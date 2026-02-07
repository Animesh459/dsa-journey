import sys
from collections import defaultdict

MOD = 10**9 + 7

def solve():
    input = sys.stdin.readline
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    cnt = defaultdict(int)
    for v in a:
        cnt[v] += 1

    cur = min(a)

    while True:
        if cnt[cur] % x != 0:
            print(pow(x, cur, MOD))
            return
        cnt[cur + 1] += cnt[cur] // x
        cur += 1


if __name__ == "__main__":
    solve()


# Examples

# Input
# 2 2
# 2 2

# Output
# 8

# Input
# 3 3
# 1 2 3

# Output
# 27

# Input
# 2 2
# 29 29

# Output
# 73741817

# Input
# 4 5
# 0 0 0 0

# Output
# 1