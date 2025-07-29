
def solve():
    row_one = -1
    col_one = -1

    for i in range(5):
        row_values = list(map(int, input().split()))
        for j in range(5):
            if row_values[j] == 1:
                row_one = i
                col_one = j

    moves = abs(row_one - 2) + abs(col_one - 2)

    print(moves)

solve()