import sys

sys.setrecursionlimit(10 ** 7)

MOD = 10 ** 9 + 7


def solve():
    input = sys.stdin.readline

    n = int(input())
    cost = list(map(int, input().split()))

    m = int(input())
    graph = [[] for _ in range(n)]
    rev_graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        rev_graph[v].append(u)

    # ---------- Kosaraju Step 1 ----------
    visited = [False] * n
    order = []

    def dfs1(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for i in range(n):
        if not visited[i]:
            dfs1(i)

    # ---------- Kosaraju Step 2 ----------
    comp = [-1] * n

    def dfs2(u, c):
        comp[u] = c
        for v in rev_graph[u]:
            if comp[v] == -1:
                dfs2(v, c)

    scc_count = 0
    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, scc_count)
            scc_count += 1

    # ---------- Process SCCs ----------
    min_cost = [float('inf')] * scc_count
    count = [0] * scc_count

    for i in range(n):
        c = comp[i]
        if cost[i] < min_cost[c]:
            min_cost[c] = cost[i]
            count[c] = 1
        elif cost[i] == min_cost[c]:
            count[c] += 1

    total_cost = sum(min_cost)
    ways = 1
    for c in range(scc_count):
        ways = (ways * count[c]) % MOD

    print(total_cost, ways)


if __name__ == "__main__":
    solve()

# Examples
#
# Input
# 3
# 1 2 3
# 3
# 1 2
# 2 3
# 3 2
#
# Output
# 3 1
#
# Input
# 5
# 2 8 0 6 0
# 6
# 1 4
# 1 3
# 2 4
# 3 4
# 4 5
# 5 1
#
# Output
# 8 2
#
# Input
# 10
# 1 3 2 2 1 3 1 4 10 10
# 12
# 1 2
# 2 3
# 3 1
# 3 4
# 4 5
# 5 6
# 5 7
# 6 4
# 7 3
# 8 9
# 9 10
# 10 9
#
# Output
# 15 6
#
# Input
# 2
# 7 91
# 2
# 1 2
# 2 1
#
# Output
# 7 1
