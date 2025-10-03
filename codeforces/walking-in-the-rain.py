import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().split()))

ans = min(max(a[i], a[i+1]) for i in range(n-1))
print(ans)

Examples

Input
4
10 3 5 10

Output
5

Input
5
10 2 8 3 5

Output
5