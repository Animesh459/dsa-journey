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

Examples
InputCopy
5
1 2 3 4 5
OutputCopy
1 1 2 3 4
InputCopy
5
2 3 4 5 6
OutputCopy
1 2 3 4 5
InputCopy
3
2 2 2
OutputCopy
1 2 2
