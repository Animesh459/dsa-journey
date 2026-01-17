def solve():
    import sys
    input = sys.stdin.readline

    n = int(input().strip())
    a = list(map(int, input().split()))

    a.sort()

    result = [1] + a[:-1]

    print(*result)


if __name__ == "__main__":
    solve()
