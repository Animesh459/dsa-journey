import sys

input = sys.stdin.readline

n = int(input())
bombs = []

for _ in range(n):
    x, y = map(int, input().split())
    bombs.append((x, y))

# Group bombs
right = []
left = []
up = []
down = []

for x, y in bombs:
    if x > 0:
        right.append((x, y))
    elif x < 0:
        left.append((x, y))
    elif y > 0:
        up.append((x, y))
    else:
        down.append((x, y))

# Sort safely
right.sort(key=lambda p: p[0])
left.sort(key=lambda p: p[0], reverse=True)
up.sort(key=lambda p: p[1])
down.sort(key=lambda p: p[1], reverse=True)

ops = []

def go(x, y):
    if x > 0:
        ops.append(f"1 {x} R")
    elif x < 0:
        ops.append(f"1 {-x} L")
    if y > 0:
        ops.append(f"1 {y} U")
    elif y < 0:
        ops.append(f"1 {-y} D")

def back(x, y):
    if y > 0:
        ops.append(f"1 {y} D")
    elif y < 0:
        ops.append(f"1 {-y} U")
    if x > 0:
        ops.append(f"1 {x} L")
    elif x < 0:
        ops.append(f"1 {-x} R")

def process(group):
    for x, y in group:
        go(x, y)
        ops.append("2")
        back(x, y)
        ops.append("3")

process(right)
process(left)
process(up)
process(down)

print(len(ops))
print("\n".join(ops))
