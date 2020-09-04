def max_pairwise_product(numbers):
    """
    Computes the product of two largest number in an array

    Args:
    numbers -- array of numbers

    Returns:
    product -- product of two largest number
    """

    first_maximum = max(numbers)
    numbers.remove(first_maximum)
    second_maximum = max(numbers)

    product = first_maximum * second_maximum

    return product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
