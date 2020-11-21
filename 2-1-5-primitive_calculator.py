import sys


def optimal_sequence(n):
    """
    Given an integer n, compute the minimum number of operations needed
    to obtain the number n starting from the number 1

    operations include: multiply by 3, multiply by 2, add by 1

    Args:
    n -- input number

    Returns:
    The minimum number of operations and all steps taken in between
    """

    min_ops = []
    min_ops_step = {}

    for _ in range(n+1):
        min_ops.append(0)

    if n >= 1:
        # don't need to anything to acheive 1 because number is assumed
        # to start at 1
        min_ops[1] = 0
    if n >= 2:
        # Can do one operation of "multiply by 2" to get to 2 from 1
        min_ops[2] = 1
    if n >= 3:
        # Can do one operation of "multiply by 3" to get to 3 from 1
        min_ops[3] = 1

    # Base case
    if n == 1 or n == 2 or n == 3:
        return str(min_ops[n]) + "\n" + str(n)

    for i in range(4, n+1):
        min_ops[i] = 1000000
        min_ops_step[i] = ""

        # Recurrence
        array = []
        if i % 3 == 0:
            array.append(int(i/3))
        if i % 2 == 0:
            array.append(int(i/2))
        array.append(i-1)

        for item in array:
            num_ops = min_ops[item] + 1
            if num_ops < min_ops[i]:
                saved_winning_number = item
                min_ops[i] = num_ops

        min_ops_step[i] = saved_winning_number

    # This is to save the result because the varible n will be
    # overwritten
    initial_input_number = n

    # The following code block is to retrive all the numbers that lead
    # to the final outcome
    all_steps = ""
    all_steps_reversed = ""

    while n != 1 and n != 2 and n != 3:
        all_steps_reversed += str(min_ops_step[n])
        all_steps_reversed += " "
        n = min_ops_step[n]

    array = all_steps_reversed.split(" ")
    j = len(array)-1

    while j >= 0:
        all_steps += array[j]
        j -= 1

    all_steps = "1"+ all_steps + str(initial_input_number)

    return str(min_ops[initial_input_number])  + "\n" + all_steps


print(optimal_sequence(1))
print(optimal_sequence(5))
print(optimal_sequence(96234))
