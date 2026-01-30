def solve():
    m = int(input())
    q_list = list(map(int, input().split()))

    # Only the smallest q matters
    q = min(q_list)

    n = int(input())
    prices = list(map(int, input().split()))

    prices.sort()

    # Prefix sums
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + prices[i]

    INF = 10 ** 18
    dp = [INF] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        # Buy normally
        dp[i] = dp[i - 1] + prices[i - 1]

        # Use discount
        if i >= q:
            free = min(2, i - q)
            j = i - q - free
            paid_sum = pref[i] - pref[i - q]
            dp[i] = min(dp[i], dp[j] + paid_sum)

    print(dp[n])


if __name__ == "__main__":
    solve()
