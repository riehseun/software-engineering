# Uses python3
import sys


def get_change(m):
    """
    Find the minimum number of coins required to return the change with
    denominators 1,3,4

    Args:
    m -- value of money

    Returns:
    The minimum number of coins
    """

    coins = set()
    coins.add(1)
    coins.add(3)
    coins.add(4)

    min_num_coins = []

    for _ in range(m+1):
        min_num_coins.append(0)

    return get_change_subroutine(m, coins, min_num_coins)



def get_change_subroutine(m, coins, min_num_coins):
    """

    """

    # Base case
    if m in coins:
        min_num_coins[m] = 1
        # print(str(m) + ":" +str(min_num_coins[m]))
        return min_num_coins[m]

    for i in range(1, m+1):
        min_num_coins[i] = 1000
        for coin in coins:
            if i >= coin:
                num_coins = get_change_subroutine(
                    i-coin, coins, min_num_coins)+1
                if num_coins < min_num_coins[i]:
                    min_num_coins[i] = num_coins

    return min_num_coins[m]




print(get_change(2))
print(get_change(3))
print(get_change(4))
print(get_change(5))
print(get_change(34))



if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
