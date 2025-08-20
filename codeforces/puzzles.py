def main():
    n, m = map(int, input().split())
    puzzles = list(map(int, input().split()))

    # Sort puzzles by number of pieces
    puzzles.sort()

    # Initialize min difference as large number
    min_diff = float('inf')

    # Check consecutive subarrays of length n
    for i in range(m - n + 1):
        diff = puzzles[i + n - 1] - puzzles[i]
        min_diff = min(min_diff, diff)

    print(min_diff)

if __name__ == "__main__":
    main()
