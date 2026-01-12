def solve():
    # read first line: n and d
    n, d = map(int, input().split())

    # read second line: coordinates
    x = list(map(int, input().split()))

    ans = 0
    j = 0

    for i in range(n):
        # move j as far as possible such that distance <= d
        while j < n and x[j] - x[i] <= d:
            j += 1

        length = j - i - 1  # number of points between i and j-1
        if length >= 2:
            ans += length * (length - 1) // 2

    print(ans)


solve()


# Examples
#
# Input
# 4 3
# 1 2 3 4
#
# Output
# 4
#
# Input
# 4 2
# -3 -2 -1 0
#
# Output
# 2
#
# Input
# 5 19
# 1 10 20 30 50
#
# Output
# 1
