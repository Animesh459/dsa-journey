n = int(input())
teams = []

# Read all team uniform colors
for _ in range(n):
    h, a = map(int, input().split())
    teams.append((h, a))

count = 0

# Check all host-guest pairs
for i in range(n):
    for j in range(n):
        if i != j:
            # If host's home matches guest's guest, increment count
            if teams[i][0] == teams[j][1]:
                count += 1

print(count)
