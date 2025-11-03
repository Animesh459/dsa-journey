def main():
    n = int(input())
    a = list(map(int, input().split()))
    moves = 0
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            moves += a[i] - a[i + 1]
    print(moves)

if __name__ == "__main__":
    main()
