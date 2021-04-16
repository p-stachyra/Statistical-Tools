import scipy.special
import numpy as np

#binominal distribution
size = float(input("Sample size: "))
p_success = float(input("P success: "))
x = float(input("X value: "))

def binominal(size, p_success, x):
	return (scipy.special.factorial(size) / (scipy.special.factorial(x) * scipy.special.factorial(size - x))) * (p_success ** x) * ((1 - p_success) ** (size -x))

print("Binominal for the value", x)
print(binominal(size, p_success, x))