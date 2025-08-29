import sys


def solve():
    """
    This function solves the "A. Exams" problem.
    It calculates the minimum number of exams with a mark of 2.
    """
    try:
        # Using input() is better for local, interactive testing.
        # It waits for the user to type a line and press Enter.
        n, k = map(int, input().split())
    except (IOError, ValueError):
        # This handles cases where input is not in the correct format.
        return

    # Let x be the number of exams with a mark of 2.
    # The remaining (n - x) exams have marks of at least 3.

    # To minimize x, we want the passing exams to contribute as much as possible.
    # The minimum possible sum from the (n-x) passing exams is 3 * (n - x).

    # The total sum k must be at least the sum from the failed exams (2*x)
    # plus the minimum possible sum from the passing exams (3*(n-x)).
    # So, k >= 2*x + 3*(n-x)
    # k >= 2x + 3n - 3x
    # k >= 3n - x
    # x >= 3n - k

    # Since the number of failed exams (x) cannot be negative, the minimum is:
    result = max(0, 3 * n - k)

    # Print the final result to the console.
    print(result)


if __name__ == "__main__":
    solve()