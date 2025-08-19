def solve():
    n, c = map(int, input().split())
    prices = list(map(int, input().split()))

    max_profit = 0
    for i in range(n - 1):
        profit = prices[i] - prices[i + 1] - c
        max_profit = max(max_profit, profit)

    print(max_profit)


if __name__ == "__main__":
    solve()
