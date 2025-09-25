import sys


def solve():
    n, k = map(int, sys.stdin.readline().split())

    if k == n:
        print(-1)
        return

    permutation = []
    # Create n-k non-good elements
    # We use a cyclic shift for the first n-k numbers
    # p_1 = 2, p_2 = 3, ..., p_{n-k-1} = n-k, p_{n-k} = 1
    # gcd(i, i+1) = 1, gcd(n-k, 1) = 1
    # This ensures n-k non-good elements

    # If n-k is 0, we can't do this. But k=n is handled already.
    # If n-k is 1, we get the permutation 1 2 3 ... n.
    # p_1 = 1, gcd(1,1)=1. This is non-good.
    # p_i = i for i>1, gcd(i,i)=i>1. These are good.
    # We get exactly n-1 good elements, which is k.

    # The construction `2, 3, ..., n-k, 1, n-k+1, ..., n` works for all k < n.
    # It covers k=n-1 (n-k=1) and k=0 (n-k=n) cases.

    for i in range(2, n - k + 1):
        permutation.append(i)

    permutation.append(1)

    for i in range(n - k + 1, n + 1):
        permutation.append(i)

    print(*permutation)


# Example usage from the problem statement:
# n=4, k=2
# n-k = 2.
# 2, 1, 3, 4
# gcd(1,2)=1, gcd(2,1)=1, gcd(3,3)=3, gcd(4,4)=4.
# 2 good elements. Correct.

# n=1, k=1
# k=n, so print -1. Correct.

solve()