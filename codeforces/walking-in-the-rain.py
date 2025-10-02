import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().split()))

ans = min(max(a[i], a[i+1]) for i in range(n-1))
print(ans)
