n, m = map(int, input().split())
rows = [input().strip() for _ in range(n)]

col_max = ['0'] * m
for j in range(m):
    mx = '0'
    for i in range(n):
        if rows[i][j] > mx:
            mx = rows[i][j]
    col_max[j] = mx

successful = 0
for i in range(n):
    if any(rows[i][j] == col_max[j] for j in range(m)):
        successful += 1

print(successful)