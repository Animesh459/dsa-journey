import sys

def main():
    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    # up[i]: farthest index reachable from i with non-decreasing sequence
    up = [0] * n
    up[-1] = n - 1
    for i in range(n - 2, -1, -1):
        if a[i] <= a[i + 1]:
            up[i] = up[i + 1]
        else:
            up[i] = i

    # down[i]: farthest index reachable from i with non-increasing sequence
    down = [0] * n
    down[-1] = n - 1
    for i in range(n - 2, -1, -1):
        if a[i] >= a[i + 1]:
            down[i] = down[i + 1]
        else:
            down[i] = i

    out = []
    for _ in range(m):
        l, r = map(int, input().split())
        l -= 1
        r -= 1

        if down[up[l]] >= r:
            out.append("Yes")
        else:
            out.append("No")

    print("\n".join(out))

if __name__ == "__main__":
    main()


# Examples
#
# Input
# 8 6
# 1 2 1 3 3 5 2 1
# 1 3
# 2 3
# 2 4
# 8 8
# 1 4
# 5 8
#
# Output
# Yes
# Yes
# No
# Yes
# No
# Yes