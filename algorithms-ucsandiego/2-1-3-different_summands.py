# Uses python3
import sys


def optimal_summands(n):
	"""
	find the maximum "k" such that "n" can be written as
	a1 + a2 + ... + ak

	Args:
	n - input number

	Returns:
	result -- array of a1, a2, ... ,ak
	"""

	# Corner case
	if n < 3:
		return [n]

	result = []

	for i in range(1,n):
		if n - sum(result) >= i + i + 1:
			result.append(i)
		else:
			result.append(n-sum(result))
			return result


print(optimal_summands(4))
print(optimal_summands(6))
print(optimal_summands(8))