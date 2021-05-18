data(cars)

# kinetic energy - proportional to squared speed
cars$sq_speed <- cars$speed ** 2

# Correlation between variables
plot(cars)

# correlation between squared speed and stopping distance
cor(cars$sq_speed, cars$dist)

# Plot squared speed and stopping distance data
plot(cars$sq_speed, 
     cars$dist, 
     main = "Stopping Distances by Speed", 
     xlab = "Speed Squared (mph ** 2)", 
     ylab = "Distance (ft)")

# model
model_stop <- lm(dist ~ 0 + sq_speed, data = cars)
summary(model_stop)

# point estimate of the slope of the prediction line
model_stop$coefficients 

# Abline the model
abline(model_stop)

# The stopping distance of interest
abline(h = 60, lty = 2, col = 'red')


# slope coefficient for 95% confidence level
confint(model_stop, level = 0.95)

# The distance of interest : somewhere around 400 (miles/h) ** 2
sq_speed <- data.frame(sq_speed = seq(0,600))

# prediction : 90% confidence interval
pred <- predict(model_stop, sq_speed, interval = "confidence", level=0.9)
#pred
sq_speed_acc <- data.frame(sq_speed = seq(350, 390, by=0.5))
pred_acc <- predict(model_hamowanie, sq_speed_acc, interval = "confidence", level=0.9)

# identify values closest to 60m
cbind(sq_speed_acc, pred_acc)

# worst scenario : safe margin
expected_max_speed <- round(sqrt(362.5))

# graphical check - approximation
matplot(sq_speed, pred, type = "l", add = TRUE)
abline(v = 363)
