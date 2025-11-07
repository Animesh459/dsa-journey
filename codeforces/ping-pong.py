from collections import deque


def can_move(A, B):
    # Check if we can move from A -> B
    return (B[0] < A[0] < B[1]) or (B[0] < A[1] < B[1])


def solve():
    n = int(input().strip())
    intervals = []

    for _ in range(n):
        query = list(map(int, input().split()))

        if query[0] == 1:
            _, x, y = query
            intervals.append((x, y))

        else:  # query[0] == 2
            _, a, b = query
            a -= 1  # to 0-based index
            b -= 1

            m = len(intervals)
            adj = [[] for _ in range(m)]

            # Build graph
            for i in range(m):
                for j in range(m):
                    if i != j and can_move(intervals[i], intervals[j]):
                        adj[i].append(j)

            # BFS to check if we can reach b from a
            visited = [False] * m
            q = deque([a])
            visited[a] = True
            reachable = False

            while q:
                u = q.popleft()
                if u == b:
                    reachable = True
                    break
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)

            print("YES" if reachable else "NO")


# Run the solver
if __name__ == "__main__":
    solve()
