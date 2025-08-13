# Read input
n, k = map(int, input().split())

# Create the table
table = [[0] * n for _ in range(n)]

# Fill diagonal with k
for i in range(n):
    table[i][i] = k

# Print the table
for row in table:
    print(" ".join(map(str, row)))