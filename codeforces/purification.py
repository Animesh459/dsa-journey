import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n = int(input())
    grid = [input().strip() for _ in range(n)]

    # Build bipartite graph: rows -> columns
    adj = [[] for _ in range(n)]
    rev = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if grid[i][j] == '.':
                adj[i].append(j)
                rev[j].append(i)

    # If any row or column has no valid cell, impossible
    for i in range(n):
        if not adj[i]:
            print(-1)
            return
    for j in range(n):
        if not rev[j]:
            print(-1)
            return

    # Hopcroft–Karp for maximum matching
    INF = 10**9
    match_row = [-1] * n
    match_col = [-1] * n
    dist = [0] * n

    def bfs():
        q = deque()
        for i in range(n):
            if match_row[i] == -1:
                dist[i] = 0
                q.append(i)
            else:
                dist[i] = INF
        d = INF

        while q:
            i = q.popleft()
            if dist[i] < d:
                for j in adj[i]:
                    if match_col[j] == -1:
                        d = dist[i] + 1
                    else:
                        if dist[match_col[j]] == INF:
                            dist[match_col[j]] = dist[i] + 1
                            q.append(match_col[j])
        return d != INF

    def dfs(i):
        for j in adj[i]:
            if match_col[j] == -1 or (
                dist[match_col[j]] == dist[i] + 1 and dfs(match_col[j])
            ):
                match_row[i] = j
                match_col[j] = i
                return True
        dist[i] = INF
        return False

    matching = 0
    while bfs():
        for i in range(n):
            if match_row[i] == -1 and dfs(i):
                matching += 1

    # Build minimum edge cover
    cover = set()

    # Add all matching edges
    for i in range(n):
        if match_row[i] != -1:
            cover.add((i, match_row[i]))

    # Unmatched rows
    for i in range(n):
        if match_row[i] == -1:
            cover.add((i, adj[i][0]))

    # Unmatched columns
    for j in range(n):
        if match_col[j] == -1:
            cover.add((rev[j][0], j))

    # Output result
    print(len(cover))
    for i, j in cover:
        print(i + 1, j + 1)

if __name__ == "__main__":
    solve()
