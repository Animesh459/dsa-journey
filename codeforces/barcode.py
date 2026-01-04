def main():
    n, m, x, y = map(int, input().split())
    grid = [input().strip() for _ in range(n)]

    # repaint cost per column
    cost_white = [0] * m  # repaint column to all '.'
    cost_black = [0] * m  # repaint column to all '#'

    for j in range(m):
        black = 0
        for i in range(n):
            if grid[i][j] == '#':
                black += 1
        cost_white[j] = black
        cost_black[j] = n - black

    # prefix sums
    pw = [0] * (m + 1)
    pb = [0] * (m + 1)

    for i in range(m):
        pw[i + 1] = pw[i] + cost_white[i]
        pb[i + 1] = pb[i] + cost_black[i]

    INF = 10**18
    dp = [[INF, INF] for _ in range(m + 1)]

    # dp[i][0] → ending with white
    # dp[i][1] → ending with black
    dp[0][0] = dp[0][1] = 0

    for i in range(1, m + 1):
        for w in range(x, y + 1):
            if i - w < 0:
                break

            dp[i][0] = min(
                dp[i][0],
                dp[i - w][1] + (pw[i] - pw[i - w])
            )

            dp[i][1] = min(
                dp[i][1],
                dp[i - w][0] + (pb[i] - pb[i - w])
            )

    print(min(dp[m][0], dp[m][1]))


if __name__ == "__main__":
    main()

# Examples
#
# Input
# 6 5 1 2
# ##.#.
# .###.
# ###..
# #...#
# .##.#
# ###..
#
# Output
# 11
#
# Input
# 2 5 1 1
# #####
# .....
#
# Output
# 5