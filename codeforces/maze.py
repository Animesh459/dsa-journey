import sys

sys.setrecursionlimit(10 ** 7)


def main():
    n, m, k = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

    empty = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                empty.append((i, j))

    s = len(empty)
    need = s - k  # number of cells to keep as '.'

    visited = [[False] * m for _ in range(n)]
    stack = []

    # find a starting empty cell
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                stack.append((i, j))
                visited[i][j] = True
                break
        if stack:
            break

    kept = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # DFS
    while stack and kept < need:
        x, y = stack.pop()
        kept += 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and grid[nx][ny] == '.':
                    visited[nx][ny] = True
                    stack.append((nx, ny))

    # turn remaining empty cells into 'X'
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.' and not visited[i][j]:
                grid[i][j] = 'X'

    # output result
    for row in grid:
        print("".join(row))


if __name__ == "__main__":
    main()
