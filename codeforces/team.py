def solve():
    n, m = map(int, input().split())

    # Check impossible cases
    if m > 2 * (n + 1) or n > m + 1:
        print(-1)
        return

    ans = []

    while n > 0 or m > 0:
        # Place ones
        if m > n:
            if m - 2 >= n and m >= 2:
                ans.append("11")
                m -= 2
            else:
                ans.append("1")
                m -= 1
        else:
            if m > 0:
                ans.append("1")
                m -= 1

        # Place zero (only one allowed at a time)
        if n > 0:
            ans.append("0")
            n -= 1

    print("".join(ans))


# Run
solve()
