def solve():
    n, d, l = map(int, input().split())

    signs = [1 if i % 2 == 0 else -1 for i in range(n)]

    min_sum = sum((1 if s == 1 else -l) for s in signs)
    max_sum = sum((l if s == 1 else -1) for s in signs)

    if not (min_sum <= d <= max_sum):
        print(-1)
        return

    a = [1 if s == 1 else l for s in signs]
    cur = min_sum

    for i in range(n):
        if cur == d:
            break
        if signs[i] == 1:
            add = min(l - a[i], d - cur)
            a[i] += add
            cur += add
        else:
            add = min(a[i] - 1, cur - d)
            a[i] -= add
            cur -= add

    print(*a)


# Only run solve() if executed directly
if __name__ == "__main__":
    solve()
