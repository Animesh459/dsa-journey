import sys


def solve():
    """
    Reads the input and checks if among the 5 people, there are either
    three pairwise acquainted or three pairwise unacquainted people.
    """
    try:
        # Read the number of relations (m)
        # Using sys.stdin.readline for potentially faster input reading
        try:
            m = int(sys.stdin.readline())
        except:
            # Handle case where m is not provided or input is empty (EOF)
            return

        # Initialize the adjacency matrix for 5 people (1-indexed for convenience)
        # matrix[i][j] = 1 if person i and j are acquainted, 0 otherwise
        # Size is 6x6, ignoring index 0
        adj = [[0] * 6 for _ in range(6)]

        # Read m acquaintance pairs
        for _ in range(m):
            try:
                # Read a pair of acquainted people (a, b)
                line = sys.stdin.readline()
                if not line:
                    break
                a, b = map(int, line.split())
            except:
                # Handle potential parsing errors
                continue

            # Since the relation is symmetrical, set both adj[a][b] and adj[b][a] to 1
            adj[a][b] = 1
            adj[b][a] = 1

    except Exception as e:
        # Handle general input/reading errors
        # print(f"An error occurred during input: {e}", file=sys.stderr)
        return

    # Iterate through all possible triplets of people (i, j, k)
    # Since there are only 5 people, there are 10 triplets: C(5, 3) = 10.
    # We use nested loops to select three distinct people.
    # We only need to check i < j < k to avoid duplicates and redundant checks.
    for i in range(1, 6):
        for j in range(i + 1, 6):
            for k in range(j + 1, 6):
                # Check for three pairwise acquainted (K3 or a clique of size 3)
                # This means all three pairs (i, j), (i, k), and (j, k) must have an acquaintance edge.
                is_acquainted_triplet = (adj[i][j] == 1 and adj[i][k] == 1 and adj[j][k] == 1)

                # Check for three pairwise unacquainted (Independent Set of size 3 or K3 in the complement graph)
                # This means none of the three pairs (i, j), (i, k), and (j, k) must have an acquaintance edge.
                is_unacquainted_triplet = (adj[i][j] == 0 and adj[i][k] == 0 and adj[j][k] == 0)

                # If either condition is met for ANY triplet, the answer is "WIN"
                if is_acquainted_triplet or is_unacquainted_triplet:
                    print("WIN")
                    return

    # If the loops complete without finding such a triplet, the answer is "FAIL"
    # This configuration is a counterexample to the statement that R(3, 3) = 5.
    print("FAIL")


# Execute the solve function
solve()


# Examples
#
# Input
# 4
# 1 3
# 2 3
# 1 4
# 5 3
#
# Output
# WIN
#
# Input
# 5
# 1 2
# 2 3
# 3 4
# 4 5
# 5 1
#
# Output
# FAIL