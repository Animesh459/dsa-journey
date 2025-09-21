import math


def get_coins(n):
    """
    Calculates the denominations of the coins.

    Args:
        n: The denomination of the most expensive coin.

    Returns:
        A list of coin denominations in decreasing order.
    """
    coins = []
    current_denomination = n
    coins.append(current_denomination)

    while current_denomination > 1:
        if current_denomination % 2 == 0:
            current_denomination //= 2
            coins.append(current_denomination)
        else:
            # Find the smallest prime factor for an odd number.
            # We can optimize by checking only odd divisors.
            smallest_prime_factor = current_denomination
            for i in range(3, int(math.sqrt(current_denomination)) + 1, 2):
                if current_denomination % i == 0:
                    smallest_prime_factor = i
                    break
            current_denomination //= smallest_prime_factor
            coins.append(current_denomination)

    return coins


if __name__ == "__main__":
    try:
        n = int(input())
        result_coins = get_coins(n)
        print(*result_coins)
    except (IOError, ValueError) as e:
        print(f"An error occurred: {e}")


# Examples
#
# Input
# 10
#
# Output
# 10 5 1
#
# Input
# 4
#
# Output
# 4 2 1
#
# Input
# 3
#
# Output
# 3 1
