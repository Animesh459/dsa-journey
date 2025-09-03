def solve():
    y, k, n = map(int, input().split())

    results = []

    m_start = (y // k + 1) * k

    m = m_start

    while m <= n:
        x = m - y
        results.append(x)
        m += k

    if not results:
        print("-1")
    else:
        print(*results)


solve()