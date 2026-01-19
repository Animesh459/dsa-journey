def rotate(x, y, a, b):
    dx = x - a
    dy = y - b
    return a - dy, b + dx   # 90-degree CCW rotation


def is_square(points):
    d = []

    # pairwise distances
    for i in range(4):
        for j in range(i + 1, 4):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            dist = dx*dx + dy*dy
            if dist == 0:
                return False
            d.append(dist)

    d.sort()
    return d[0] == d[1] == d[2] == d[3] and d[4] == d[5]


def solve():
    n = int(input())

    for _ in range(n):
        moles = []
        for _ in range(4):
            x, y, a, b = map(int, input().split())
            moles.append((x, y, a, b))

        best = float('inf')

        # Try all 4^4 rotation combinations
        for r0 in range(4):
            x0, y0, a0, b0 = moles[0]
            for _ in range(r0):
                x0, y0 = rotate(x0, y0, a0, b0)

            for r1 in range(4):
                x1, y1, a1, b1 = moles[1]
                for _ in range(r1):
                    x1, y1 = rotate(x1, y1, a1, b1)

                for r2 in range(4):
                    x2, y2, a2, b2 = moles[2]
                    for _ in range(r2):
                        x2, y2 = rotate(x2, y2, a2, b2)

                    for r3 in range(4):
                        x3, y3, a3, b3 = moles[3]
                        for _ in range(r3):
                            x3, y3 = rotate(x3, y3, a3, b3)

                        if is_square([(x0, y0), (x1, y1), (x2, y2), (x3, y3)]):
                            best = min(best, r0 + r1 + r2 + r3)

        print(best if best != float('inf') else -1)


solve()
