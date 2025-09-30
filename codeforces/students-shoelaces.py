import sys


# Set recursion limit higher for safety, though not strictly needed here
# sys.setrecursionlimit(2000)

def solve():
    """
    Simulates the process of kicking out students tied to exactly one other student
    in simultaneous groups until no more such students can be found.
    """
    try:
        # Read the first line for n and m using standard input reading
        line = sys.stdin.readline()
        if not line:
            return

        n, m = map(int, line.split())
    except Exception:
        return

    # If no students or no laces, no groups will be kicked out
    if n <= 1 or m == 0:
        print(0)
        return

    # Adjacency list: adj[i] is a set of neighbors for student i (0-based)
    adj = [set() for _ in range(n)]
    # Initial degree list
    degree = [0] * n

    # Read the m lace connections
    for _ in range(m):
        try:
            line = sys.stdin.readline()
            if not line:
                break
            # Students are 1-based in input, convert to 0-based
            u, v = map(int, line.split())
            u -= 1
            v -= 1
        except Exception:
            continue

        # Add edges (only if valid input)
        if 0 <= u < n and 0 <= v < n and u != v:
            adj[u].add(v)
            adj[v].add(u)
            degree[u] += 1
            degree[v] += 1

    # Counter for the number of groups kicked out
    groups_kicked_out = 0

    while True:
        # Step 1: Find all students with degree 1 to be kicked out *simultaneously*
        students_to_kick = []
        for i in range(n):
            # We only consider students who are still 'active' (degree[i] > -1)
            # A degree of 1 means they are reprimanded.
            if degree[i] == 1:
                students_to_kick.append(i)

        # If no students are reprimanded, the process stops
        if not students_to_kick:
            break

        # A group is kicked out
        groups_kicked_out += 1

        # Step 2: Process the removal and update neighbors' degrees
        for u in students_to_kick:
            # Mark the student u as removed (e.g., degree set to -1)
            degree[u] = -1

            # Since degree[u] was 1, it has exactly one neighbor.
            # Pop the only neighbor 'v' from u's adjacency set.
            # We need to iterate over a copy of the set or list since we are modifying it.
            # *Crucially*, we must handle the case where the only neighbor 'v' was also
            # in the group being kicked out (students_to_kick).

            # Since u was degree 1, there is exactly one element in adj[u].
            # Using list(adj[u])[0] is safe here.

            # Handle the neighbor update
            if adj[u]:  # Ensure the set is not empty (defensive check)
                v = list(adj[u])[0]

                # If the neighbor 'v' is NOT being kicked out in this group
                if degree[v] > 0:
                    # Remove the connection from v's side
                    if u in adj[v]:
                        adj[v].remove(u)
                    # Decrease v's degree
                    degree[v] -= 1

            # Clear u's adjacency list (u is gone)
            adj[u].clear()

    # Final result output
    print(groups_kicked_out)


if __name__ == "__main__":
    # Ensure correct execution by redirecting to solve function
    solve()