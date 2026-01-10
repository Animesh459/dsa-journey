def max_lcm_of_three(n: int) -> int:
    if n <= 2:
        return n

    if n % 2 == 1:
        # n is odd
        return n * (n - 1) * (n - 2)
    else:
        # n is even
        if n % 3 != 0:
            return n * (n - 1) * (n - 3)
        else:
            return (n - 1) * (n - 2) * (n - 3)


if __name__ == "__main__":
    n = int(input().strip())
    print(max_lcm_of_three(n))


# Examples
#
# Input
# 9
#
# Output
# 504
#
# Input
# 7
#
# Output
# 210