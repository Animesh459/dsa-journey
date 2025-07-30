def solve():
    n = int(input())
    a = list(map(int, input().split()))

    max_height = 0
    min_height = 101

    for height in a:
        if height > max_height:
            max_height = height
        if height < min_height:
            min_height = height

    idx_max = -1
    idx_min = -1

    for i in range(n):
        if a[i] == max_height:
            idx_max = i
            break

    for i in range(n - 1, -1, -1):
        if a[i] == min_height:
            idx_min = i
            break

    total_moves = idx_max + ((n - 1) - idx_min)

    if idx_max > idx_min:
        total_moves -= 1

    print(total_moves)


solve()