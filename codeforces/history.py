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
