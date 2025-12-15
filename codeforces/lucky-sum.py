def main():
    n = int(input().strip())

    best_x = -1
    best_y = -1

    # Try all possible counts of 7s
    for y in range(n // 7 + 1):
        remaining = n - 7 * y
        if remaining >= 0 and remaining % 4 == 0:
            x = remaining // 4
            # Choose maximum number of 4s for minimum number
            if x > best_x:
                best_x = x
                best_y = y

    if best_x == -1:
        print(-1)
    else:
        print("4" * best_x + "7" * best_y)


if __name__ == "__main__":
    main()
