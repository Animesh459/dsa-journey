import sys
sys.setrecursionlimit(300000)

def main():
    n = int(sys.stdin.readline())
    g = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        g[u].append(v)
        g[v].append(u)

    init = [0] + list(map(int, sys.stdin.readline().split()))
    goal = [0] + list(map(int, sys.stdin.readline().split()))

    visited = [False] * (n + 1)
    ans = []

    # DFS: depth 0 = root (even)
    def dfs(node, depth, flip_even, flip_odd):
        visited[node] = True

        # Determine effective value after flips
        if depth % 2 == 0:
            current = init[node] ^ flip_even
        else:
            current = init[node] ^ flip_odd

        # If mismatch -> we need to flip node
        if current != goal[node]:
            ans.append(node)
            if depth % 2 == 0:
                flip_even ^= 1
            else:
                flip_odd ^= 1

        # Continue DFS
        for nxt in g[node]:
            if not visited[nxt]:
                dfs(nxt, depth + 1, flip_even, flip_odd)

    dfs(1, 0, 0, 0)

    # Output
    print(len(ans))
    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()
