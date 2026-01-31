def main():
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().split())

    # Maximum possible tot
    max_tot = n * (n - 1) // 2

    if max_tot <= k:
        print("no solution")
        return

    # All points share the same x-coordinate
    # y is strictly increasing to ensure uniqueness
    for i in range(n):
        print(0, i)


if __name__ == "__main__":
    main()
