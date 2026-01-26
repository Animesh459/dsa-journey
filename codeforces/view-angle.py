import sys
import math

def main():
    input = sys.stdin.readline
    n = int(input())

    angles = []
    for _ in range(n):
        x, y = map(int, input().split())
        angle = math.degrees(math.atan2(y, x))
        if angle < 0:
            angle += 360
        angles.append(angle)

    # If only one mannequin, angle needed is 0
    if n == 1:
        print("0.0000000000")
        return

    angles.sort()

    extended = angles + [a + 360 for a in angles]

    max_gap = 0.0
    for i in range(len(extended) - 1):
        max_gap = max(max_gap, extended[i + 1] - extended[i])

    answer = 360.0 - max_gap
    print(f"{answer:.10f}")

if __name__ == "__main__":
    main()

# Examples

# Input
# 2
# 2 0
# 0 2

# Output
# 90.0000000000

# Input
# 3
# 2 0
# 0 2
# -2 2

# Output
# 135.0000000000

# Input
# 4
# 2 0
# 0 2
# -2 0
# 0 -2

# Output
# 270.0000000000

# Input
# 2
# 2 1
# 1 2

# Output
# 36.8698976458
