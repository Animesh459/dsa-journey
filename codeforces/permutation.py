import sys


def solve():
    """
    Constructs a permutation 'a' of length 2n that satisfies the equation.
    It uses a simple pattern of swapping the first k pairs of consecutive integers.
    """
    try:
        # Read n and k. Using sys.stdin.readline is generally faster.
        line = sys.stdin.readline()
        if not line:
            return

        # Parse the two integers
        n, k = map(int, line.split())
    except Exception:
        # Handle potential parsing issues
        return

    # The resulting permutation list. Pre-allocating can be slightly faster.
    a = []

    # Iterate through the n pairs, indexed i from 0 to n-1.
    # The numbers in the i-th pair are (2*i + 1) and (2*i + 2).

    # 1. First k pairs: SWAP
    # The larger number (2*i + 2) comes first. Difference d_i = 1.
    for i in range(k):
        num1 = 2 * i + 1
        num2 = 2 * i + 2

        # Append [2i+2, 2i+1]
        a.append(num2)
        a.append(num1)

    # 2. Remaining n-k pairs: NO SWAP
    # The smaller number (2*i + 1) comes first. Difference d_i = -1.
    for i in range(k, n):
        num1 = 2 * i + 1
        num2 = 2 * i + 2

        # Append [2i+1, 2i+2]
        a.append(num1)
        a.append(num2)

    # Output the result as a space-separated string
    sys.stdout.write(" ".join(map(str, a)) + "\n")


if __name__ == "__main__":
    # Ensure standard output is used correctly
    solve()