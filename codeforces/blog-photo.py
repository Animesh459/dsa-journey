import sys
import math

def ok_ratio(h, w):
    return 0.8 <= h / w <= 1.25

def solve():
    h, w = map(int, sys.stdin.readline().split())

    best_area = 0
    best_h = 0
    best_w = 0

    # Powers of two up to 2^30 (since max dimension is 1e9)
    powers = []
    x = 1
    while x <= max(h, w):
        powers.append(x)
        x <<= 1

    for p in powers:
        # Case 1: height = p
        if p <= h:
            # width must satisfy ratio constraints and be <= w
            low_w = math.ceil(p / 1.25)
            high_w = math.floor(p / 0.8)
            if low_w <= high_w:
                W = min(w, high_w)
                if W >= low_w:
                    area = p * W
                    if (area > best_area) or (area == best_area and p > best_h):
                        best_area = area
                        best_h = p
                        best_w = W

        # Case 2: width = p
        if p <= w:
            low_h = math.ceil(p * 0.8)
            high_h = math.floor(p * 1.25)
            if low_h <= high_h:
                H = min(h, high_h)
                if H >= low_h:
                    area = p * H
                    if (area > best_area) or (area == best_area and H > best_h):
                        best_area = area
                        best_h = H
                        best_w = p

    print(best_h, best_w)


if __name__ == "__main__":
    solve()
