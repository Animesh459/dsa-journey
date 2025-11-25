# Read n and m
n, m = map(int, input().split())

# Read volunteer names
names = [input().strip() for _ in range(n)]
name_to_index = {name: i for i, name in enumerate(names)}

# Initialize compatibility matrix
compat = [[True]*n for _ in range(n)]
for i in range(n):
    compat[i][i] = True

# Read incompatible pairs
for _ in range(m):
    a, b = input().split()
    i, j = name_to_index[a], name_to_index[b]
    compat[i][j] = compat[j][i] = False

best_team = []

# Try all subsets using bitmask
for mask in range(1, 1 << n):
    team = [i for i in range(n) if mask & (1 << i)]
    ok = True
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            if not compat[team[i]][team[j]]:
                ok = False
                break
        if not ok:
            break
    if ok and len(team) > len(best_team):
        best_team = team

# Print the result
result_names = sorted(names[i] for i in best_team)
print(len(result_names))
for name in result_names:
    print(name)
