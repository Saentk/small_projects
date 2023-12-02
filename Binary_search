def binary_search(item):
	high = len(list_for_search) - 1
	low = 0
	while low <= high:
		mid = (high + low) // 2
		guess = list_for_search[mid]
		if guess == item:
			return guess
		elif item < guess:
			high = mid - 1
		else:
			low = mid + 1
	else:
		return False

list_for_search = range(1, 101, 2)

for x in range(1, 100):
	print(binary_search(x))

