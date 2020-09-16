# Uses python3
import sys


def lcm_naive(a, b):
	"""
	Finds the least common multiple

	Args:
	a -- first number
	b -- second number

	Returns:
	least common multiple
	"""

	# Swap such that "b" is always greater than "a"
    if a > b:
    	temp = a
    	a = b
    	b = temp

    i = 1
    while i <= a:
    	if b * i % a == 0:
    		return b * i
    	i += 1

    return 0


print(lcm_naive(6, 8))
print(lcm_naive(761457, 614573))