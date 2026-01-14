def xor_upto(k):
    # XOR of all numbers from 1 to k
    if k % 4 == 0:
        return k
    elif k % 4 == 1:
        return 1
    elif k % 4 == 2:
        return k + 1
    else:
        return 0


def solve():
    import sys
    input = sys.stdin.readline

    n = int(input())
    p = list(map(int, input().split()))

    ans = 0

    # XOR all p[i]
    for x in p:
        ans ^= x

    # Apply magic formula
    for i in range(1, n + 1):
        full = n // i
        rem = n % i

        if full % 2 == 1:
            ans ^= xor_upto(i)

        ans ^= xor_upto(rem)

    print(ans)


if __name__ == "__main__":
    solve()
