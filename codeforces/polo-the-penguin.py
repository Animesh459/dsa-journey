def main():
    n, m, d = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.extend(map(int, input().split()))

    # Check if all elements have same remainder mod d
    rem = arr[0] % d
    for num in arr:
        if num % d != rem:
            print(-1)
            return

    # Sort and find median
    arr.sort()
    median = arr[len(arr)//2]

    # Count total moves
    moves = 0
    for num in arr:
        moves += abs(num - median) // d

    print(moves)

if __name__ == "__main__":
    main()
