def solve():
    import sys

    line = sys.stdin.readline().strip()
    if not line:
        # no input, must print something according to problem rules
        print(0, 0)
        return

    n = int(line)
    arr = list(map(int, sys.stdin.readline().split()))

    orig = list(range(1, n + 1))

    # find leftmost mismatch
    l = 0
    while l < n and arr[l] == orig[l]:
        l += 1

    # already identical -> no valid reversal
    if l == n:
        print(0, 0)
        return

    # find rightmost mismatch
    r = n - 1
    while r >= 0 and arr[r] == orig[r]:
        r -= 1

    # try reversing
    rev = arr[:]
    rev[l:r + 1] = reversed(rev[l:r + 1])

    if rev == orig:
        print(l + 1, r + 1)
    else:
        print(0, 0)


if __name__ == "__main__":
    solve()
