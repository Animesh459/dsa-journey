def solve():
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]

    # Build prefix sums of occupied cells for each column
    prefix = [[0] * (n + 1) for _ in range(m)]
    for i in range(n):
        for j in range(m):
            prefix[j][i + 1] = prefix[j][i] + (grid[i][j] == '1')

    max_perim = 0

    # Try all row pairs
    for top in range(n):
        for bottom in range(top, n):
            good = []
            for j in range(m):
                # check if column j has any 1s between rows top..bottom
                occ = prefix[j][bottom + 1] - prefix[j][top]
                good.append(occ == 0)

            # find longest stretch of True values
            width = 0
            for val in good:
                if val:
                    width += 1
                    height = bottom - top + 1
                    max_perim = max(max_perim, 2 * (width + height))
                else:
                    width = 0

    print(max_perim)

solve()
