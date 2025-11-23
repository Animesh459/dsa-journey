def solve():
    import sys
    sys.setrecursionlimit(10**7)

    n, m = map(int, sys.stdin.readline().split())
    g = [list(sys.stdin.readline().strip()) for _ in range(n)]

    blacks = [(i, j) for i in range(n) for j in range(m) if g[i][j] == 'B']

    # --- Connectivity check ---
    from collections import deque
    visited = [[False] * m for _ in range(n)]

    # BFS from first black cell
    q = deque([blacks[0]])
    visited[blacks[0][0]][blacks[0][1]] = True
    cnt = 1

    while q:
        x, y = q.popleft()
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and g[nx][ny] == 'B':
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1

    if cnt != len(blacks):
        print("NO")
        return

    # --- Row convexity ---
    for i in range(n):
        cols = [j for j in range(m) if g[i][j] == 'B']
        if cols:
            if max(cols) - min(cols) + 1 != len(cols):
                print("NO")
                return

    # --- Column convexity ---
    for j in range(m):
        rows = [i for i in range(n) if g[i][j] == 'B']
        if rows:
            if max(rows) - min(rows) + 1 != len(rows):
                print("NO")
                return

    print("YES")

solve()