from collections import deque
import sys

def main():
    input = sys.stdin.readline

    x0, y0, x1, y1 = map(int, input().split())
    n = int(input())

    allowed = set()

    for _ in range(n):
        r, a, b = map(int, input().split())
        for c in range(a, b + 1):
            allowed.add((r, c))

    queue = deque()
    queue.append((x0, y0, 0))

    visited = set()
    visited.add((x0, y0))

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    while queue:
        x, y, dist = queue.popleft()

        if (x, y) == (x1, y1):
            print(dist)
            return

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) in allowed and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))

    print(-1)


if __name__ == "__main__":
    main()


# Examples

# Input
# 5 7 6 11
# 3
# 5 3 8
# 6 7 11
# 5 2 5

# Output
# 4

# Input
# 3 4 3 10
# 3
# 3 1 4
# 4 5 9
# 3 10 10

# Output
# 6
# Input
# 1 1 2 10
# 2
# 1 1 3
# 2 6 10

# Output
# -1