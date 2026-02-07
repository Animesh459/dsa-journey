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
