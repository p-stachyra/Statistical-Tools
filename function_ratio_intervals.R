library(tolerance)
x_6 <- rnorm(6,100,25)
x_30 <- rnorm(30,100,25)
x_150 <- rnorm(150,100,25)

ratio_intervals <- function(norm_dist, conf_level) {
  prediction_limits <- mean(norm_dist) + c(-1,1) * qt(0.9, length(norm_dist) - 1) * sd(norm_dist) * sqrt(1/length(norm_dist)+1)
  tol_interval <- normtol.int(norm_dist, alpha=conf_level, P=0.8, side=2)
  pred_interval_len <- prediction_limits[2] - prediction_limits[1]
  tol_interval_len <- tol_interval$'2-sided.upper' - tol_interval$'2-sided.lower'
  return (tol_interval_len / pred_interval_len)
}

ratio6_95 <- ratio_intervals(x_6, 0.05)
ratio6_99 <- ratio_intervals(x_6, 0.01)
ratio30_95 <- ratio_intervals(x_30, 0.05)
ratio30_99 <- ratio_intervals(x_30, 0.01)
ratio150_95 <- ratio_intervals(x_150, 0.05)
ratio150_99 <- ratio_intervals(x_150, 0.01)

ratio6_95
ratio6_99
ratio30_95
ratio30_99
ratio150_95
ratio150_99

normtol.int(x_186, alpha=0.05, P=0.8, side=2)
x_36 <- append(x_6, x_30)
x_186 <- append(x_36, x_150)
plot(x_186)
abline(h=mean(c(mean(x_6), mean(x_30), mean(x_150))),col = 'red')

