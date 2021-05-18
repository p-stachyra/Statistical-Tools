import numpy as np
import math
import sys

string = input("Provide the collection of values:\n > ")
string2 = string.replace(" ", ",")
print(string2)

def sort_it(string2):
	arr = string2.split(",")
	arr = np.array(arr).astype(float)
	arr.sort()
	return arr

def count_median(arr):
	position = 0.5 * (len(arr) + 1)
	print(f"Place of median: {position}")
	position1 = math.floor(position) - 1
	position2 = math.floor(position)
	val1 = arr[position1]
	val2 = arr[position2]
	return np.mean([val1, val2])

def count_variance(arr, how='pop'):
	diff = 0
	difference = []
	if how == 'pop':
		lenght = len(arr)
	elif how == 'smpl':
		lenght = len(arr) - 1
	for val in arr:
		difference.append(val - np.mean(arr))
		diff += (val - np.mean(arr)) ** 2
	return diff, (diff / lenght), difference

arr = sort_it(string2)

if __name__ == '__main__':
	arr = sort_it(string2)
	print(f"\nLenght: {len(arr)}")
	print(f"Sum of all elements: {sum(arr)}")
	print(f"Median: {count_median(arr)}")
	print(f"\nMean: {np.mean(arr)}")
	print(f"Sum of squared differences: {count_variance(arr)[0]}")
	print("x - mean:", count_variance(arr, how='pop')[2])
	print(f"Variance [ sum((val - mean) ** 2) / length ] : {count_variance(arr)[1]}")
	print(f"Standard deviation: {np.sqrt(count_variance(arr)[1])}")
	print(f"Coefficient of Variation [in percent]: {np.sqrt(count_variance(arr)[1]) / np.mean(arr) * 100}")
	print(f"\n\n[SAMPLE] Variance [ sum((val - mean) ** 2) / length - 1 ] : {count_variance(arr, how='smpl')[1]}")
	print(f"[SAMPLE] Standard deviation: {np.sqrt(count_variance(arr, how='smpl')[1])}")
	print(f"[SAMPLE] Coefficient of Variation [in percent]: {np.sqrt(count_variance(arr, how='smpl')[1]) / np.mean(arr) * 100}")
