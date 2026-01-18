def main():
    import sys
    input = sys.stdin.readline

    n, l, r, Ql, Qr = map(int, input().split())
    w = list(map(int, input().split()))

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + w[i]

    INF = 10 ** 30
    best = INF

    for left in range(n + 1):
        right = n - left

        cost = prefix[left] * l + (prefix[n] - prefix[left]) * r

        if left > right:
            cost += (left - right - 1) * Ql
        elif right > left:
            cost += (right - left - 1) * Qr

        best = min(best, cost)

    print(best)


if __name__ == "__main__":
    main()
