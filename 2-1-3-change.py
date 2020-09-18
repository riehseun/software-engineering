# Uses python3
import sys

def get_change(m):
    """
	Finds the minimum number of coins needed to change the input value

	Args:
	m -- input value

	Returns
	denominations -- minimum number of coins needed
    """

    denominations = 0

    if m >= 10:
    	remainder = m % 10
    	denominations += int((m - remainder) / 10)
    	m = remainder
    if m >= 5:
    	remainder = m % 5
    	denominations += int((m - remainder) / 5)
    	m = remainder
    if m < 5:
    	denominations += m

    return denominations


print(get_change(2))
print(get_change(28))
