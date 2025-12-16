def solve():
    import sys
    input = sys.stdin.readline

    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    if n == 1:
        print(-1)
        return

    if n == 2:
        a, b = arr
        if a == b:
            print(1)
            print(a)
            return

        d = b - a
        res = {a - d, b + d}
        if d % 2 == 0:
            res.add(a + d // 2)

        res = sorted(res)
        print(len(res))
        print(*res)
        return

    diffs = []
    for i in range(1, n):
        diffs.append(arr[i] - arr[i - 1])

    unique_diffs = set(diffs)

    if len(unique_diffs) > 2:
        print(0)
        return

    if len(unique_diffs) == 1:
        d = diffs[0]
        print(2)
        print(arr[0] - d, arr[-1] + d)
        return

    d1, d2 = sorted(unique_diffs)
    if d2 != 2 * d1:
        print(0)
        return

    if diffs.count(d2) > 1:
        print(0)
        return

    for i in range(1, n):
        if arr[i] - arr[i - 1] == d2:
            print(1)
            print(arr[i - 1] + d1)
            return


if __name__ == "__main__":
    solve()
