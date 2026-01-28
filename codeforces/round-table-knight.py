def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    moods = list(map(int, data[1:]))

    # Try all possible step sizes
    for k in range(1, n):
        if n % k != 0:
            continue

        # Polygon must have at least 3 vertices
        if n // k < 3:
            continue

        # Check all possible starting positions
        for start in range(k):
            ok = True
            for j in range(start, n, k):
                if moods[j] == 0:
                    ok = False
                    break
            if ok:
                print("YES")
                return

    print("NO")


if __name__ == "__main__":
    main()
