def main():
    import sys
    input = sys.stdin.readline

    n, b = map(int, input().split())
    a = list(map(int, input().split()))

    ans = b  # best if he never buys/sells

    for i in range(n):
        # buy at day i
        buy_price = a[i]
        dollars = b // buy_price
        if dollars == 0:
            continue
        cost = dollars * buy_price

        for j in range(i + 1, n):
            # sell at day j
            sell_price = a[j]
            money = b - cost + dollars * sell_price
            if money > ans:
                ans = money

    print(ans)


if __name__ == "__main__":
    main()
