import sys


def solve():
    # Read n and x0
    try:
        line = sys.stdin.readline().split()
        if not line:
            return
        n = int(line[0])
        x0 = int(line[1])
    except EOFError:
        return

    segments = []
    # Read the n segments
    for _ in range(n):
        try:
            line = sys.stdin.readline().split()
            if not line:
                break
            a = int(line[0])
            b = int(line[1])
            # Normalize the segment
            segments.append((min(a, b), max(a, b)))
        except EOFError:
            break
        except ValueError:
            break

    if len(segments) != n:
        return

    # Initialize L and R for the intersection
    L = 0
    R = 1000

    for start, end in segments:
        L = max(L, start)
        R = min(R, end)

    # Check if a common position exists
    if L > R:
        print("-1")
        return

    # Find the minimum distance

    # x0 is within the valid range [L, R]
    if L <= x0 <= R:
        min_distance = 0

    # x0 is to the left of the valid range (x0 < L)
    elif x0 < L:
        min_distance = L - x0

    # x0 is to the right of the valid range (x0 > R)
    else:  # x0 > R
        min_distance = x0 - R

    print(min_distance)


solve()