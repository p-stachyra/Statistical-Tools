import numpy as np 

weights = input("Weights:\n > ")
probabilities = input("Collections of P(x):\n > ")

weights = np.array(weights.split(" ")).astype(float)
probabilities = np.array(probabilities.split(" ")).astype(float)

multiplied = weights * probabilities
print("\n\n-------------------------------------")
print(f"\n----- x * P(x) -----\n")
print("-------------------------------------")
for val in multiplied:
	print(f"{val} ", end=" ")
print()
print()
expected_value = sum(multiplied)

general_diff_multiplied = 0
index = 1
for prob,val in zip(probabilities, weights):
	diff_sq = (val - expected_value) ** 2
	print(f"[{index}] Squared difference between weight and expected value: {diff_sq}")
	diff_multiplied = diff_sq * prob
	general_diff_multiplied += diff_multiplied
	print(f"[{index}] Squared difference * probability: {diff_multiplied}")
	index += 1

var = general_diff_multiplied
std = np.sqrt(general_diff_multiplied)

print(f"\nThe expected value: {expected_value}")
print(f"The variance: {var}")
print(f"The standard deviation: {std}")

