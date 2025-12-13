import sys

def main():
    input = sys.stdin.readline
    n = int(input())

    board = [list(map(int, input().split())) for _ in range(n)]

    # There are 2n-1 diagonals of each type
    main_diag = [0] * (2 * n)
    anti_diag = [0] * (2 * n)

    # Precompute diagonal sums
    for i in range(n):
        for j in range(n):
            main_diag[i - j + n] += board[i][j]
            anti_diag[i + j] += board[i][j]

    best_black = 0
    best_white = 0
    black_pos = (1, 1)
    white_pos = (1, 1)

    # Evaluate each cell
    for i in range(n):
        for j in range(n):
            total = main_diag[i - j + n] + anti_diag[i + j] - board[i][j]

            if (i + j) % 2 == 0:
                if total > best_black:
                    best_black = total
                    black_pos = (i + 1, j + 1)
            else:
                if total > best_white:
                    best_white = total
                    white_pos = (i + 1, j + 1)

    print(best_black + best_white)
    print(black_pos[0], black_pos[1], white_pos[0], white_pos[1])

if __name__ == "__main__":
    main()
