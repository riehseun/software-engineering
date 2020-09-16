# Uses python3
def calc_fib(n):
	"""
	Implments efficient algorithm for finding nth number in Fibonacci
	sequence

	Args:
	n -- specifies which Fibonacci number to find

	Returns:
	number -- nth number of Fibonacci sequence
	"""

	# Handle corner cases
	if n == 0:
		return 0
	elif n == 1:
		return 1

	# Initialize array to store Fibonacci sequence
	fib_array = []
	for i in range(n):
		fib_array.append(0)

	fib_array[0] = 1
	fib_array[1] = 1
	for i in range(2,n):
		fib_array[i] = fib_array[i-1] + fib_array[i-2]

	number = fib_array[n-1]
	return number


print(calc_fib(10))