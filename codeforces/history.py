n = int(input())

events = []
for _ in range(n):
    a, b = map(int, input().split())
    events.append((a, b))

# Sort by start year
events.sort(key=lambda x: x[0])

max_end = -1
included_count = 0

for a, b in events:
    if b < max_end:
        included_count += 1
    else:
        max_end = b

print(included_count)

# Examples
#
# Input
# 5
# 1 10
# 2 9
# 3 8
# 4 7
# 5 6
#
# Output
# 4
#
# Input
# 5
# 1 100
# 2 50
# 51 99
# 52 98
# 10 60
#
# Output
# 4
#
# Input
# 1
# 1 1000000000
#
# Output
# 0