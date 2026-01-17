def solve():
    import sys
    input = sys.stdin.readline

    n = int(input().strip())
    a = list(map(int, input().split()))

    a.sort()

    # Always insert 1 at front + shift others
    result = [1] + a[:-1]

    print(*result)


if __name__ == "__main__":
    solve()
