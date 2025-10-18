m, n = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(m)]

# Step 1: Start with all ones
A = [[1] * n for _ in range(m)]

# Step 2: For each B[i][j] == 0, set row i and column j to 0
for i in range(m):
    for j in range(n):
        if B[i][j] == 0:
            for k in range(n):
                A[i][k] = 0
            for k in range(m):
                A[k][j] = 0

# Step 3: Reconstruct B' from A
B_check = [[0] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        row_or = any(A[i][k] for k in range(n))
        col_or = any(A[k][j] for k in range(m))
        B_check[i][j] = int(row_or or col_or)

# Step 4: Compare B' with B
if B_check == B:
    print("YES")
    for row in A:
        print(*row)
else:
    print("NO")
