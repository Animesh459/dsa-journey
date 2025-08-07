r, c = map(int, input().split())
cake = [list(input()) for _ in range(r)]

eaten = [[False] * c for _ in range(r)]
count = 0

# Eat full rows without 'S'
for i in range(r):
    if 'S' not in cake[i]:
        for j in range(c):
            if not eaten[i][j]:
                eaten[i][j] = True
                count += 1

# Eat full columns without 'S'
for j in range(c):
    has_strawberry = False
    for i in range(r):
        if cake[i][j] == 'S':
            has_strawberry = True
            break
    if not has_strawberry:
        for i in range(r):
            if not eaten[i][j]:
                eaten[i][j] = True
                count += 1

print(count)
