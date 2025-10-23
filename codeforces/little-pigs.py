import sys


def solve():
    # Read n and m from the first line
    try:
        # Read the first line and split it
        line = sys.stdin.readline()
        if not line:
            return
        n, m = map(int, line.split())
    except:
        return

    # Read the grid row by row
    grid = []
    for _ in range(n):
        # Read n subsequent lines for the grid
        grid.append(sys.stdin.readline().strip())

    eaten_pigs = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Iterate through the grid
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 'W':

                # Check neighbors for a pig
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < n and 0 <= nc < m:
                        if grid[nr][nc] == 'P':
                            eaten_pigs += 1
                            # Wolf has eaten one pig; move to the next wolf
                            break

    print(eaten_pigs)


if __name__ == "__main__":
    # Ensure standard input stream is available for reading
    if not sys.stdin.isatty():
        solve()
    else:
        # This branch is usually for interactive testing; use the existing function
        solve()