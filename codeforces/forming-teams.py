def main():
    import sys
    sys.setrecursionlimit(10000)
    n, m = map(int, sys.stdin.readline().split())

    g = [[] for _ in range(n)]

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    visited = [False] * n
    odd_cycles = 0

    def dfs(u, parent):
        visited[u] = True
        for v in g[u]:
            if v == parent:
                continue
            if not visited[v]:
                if dfs(v, u):
                    return True
            else:
                # If visited and not parent: cycle detected
                return True
        return False

    for i in range(n):
        if not visited[i]:
            # Traverse component and count nodes
            comp = []
            stack = [i]
            visited2 = [False] * n
            visited2[i] = True

            while stack:
                u = stack.pop()
                comp.append(u)
                for v in g[u]:
                    if not visited2[v]:
                        visited2[v] = True
                        stack.append(v)

            # Now check if this component is a cycle:
            # A cycle component must have all degrees == 2
            is_cycle = all(len(g[x]) == 2 for x in comp)
            if is_cycle:
                # Check odd cycle (size odd)
                if len(comp) % 2 == 1:
                    odd_cycles += 1

            # Mark whole component as visited in main array
            for x in comp:
                visited[x] = True

    # Compute final answer
    remaining = n - odd_cycles
    if remaining % 2 == 1:
        odd_cycles += 1

    print(odd_cycles)


if __name__ == "__main__":
    main()
