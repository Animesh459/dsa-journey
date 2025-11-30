import sys
import threading

def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    pts = [tuple(map(int, input().split())) for _ in range(n)]

    def cross(a, b, c):
        # cross product (b-a) x (c-a)
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

    best = 0.0

    for i in range(n):
        for j in range(i + 1, n):
            max_left = 0
            max_right = 0
            A = pts[i]
            B = pts[j]

            for k in range(n):
                if k == i or k == j:
                    continue
                cr = cross(A, B, pts[k])
                if cr > 0:          # left side
                    if cr > max_left:
                        max_left = cr
                else:               # right side
                    cr = -cr        # store positive value
                    if cr > max_right:
                        max_right = cr

            total = max_left + max_right
            if total > best:
                best = total

    # best is twice the real area
    print(best / 2)


if __name__ == "__main__":
    threading.Thread(target=main).start()
