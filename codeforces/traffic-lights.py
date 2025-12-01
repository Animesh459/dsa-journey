import sys
import math

def main():
    l, d, v, g, r = map(int, sys.stdin.readline().split())

    t1 = d / v
    cycle = g + r
    pos = t1 % cycle

    if pos <= g:
        wait = 0
    else:
        wait = cycle - pos

    ans = t1 + wait + (l - d) / v
    print(f"{ans:.10f}")

if __name__ == "__main__":
    main()
