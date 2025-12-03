def main():
    import sys
    input = sys.stdin.readline

    n = int(input().strip())
    a = list(map(int, input().split()))

    total = sum(a)

    # If total cannot be divided into 3 equal parts
    if total % 3 != 0:
        print(0)
        return

    S = total // 3
    S2 = 2 * S

    prefix = 0
    count_S = 0
    ways = 0

    # Traverse until n-1 for checking 2S, until n-2 for counting S
    for i in range(n - 1):
        prefix += a[i]

        # If prefix == 2S and we're not at the last index
        if prefix == S2 and i < n - 1:
            ways += count_S

        # Count occurrences of S only before the last 2 positions
        if prefix == S:
            count_S += 1

    print(ways)


if __name__ == "__main__":
    main()
