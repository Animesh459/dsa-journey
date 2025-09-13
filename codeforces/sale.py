n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(m):
  if a[i] < 0:
    ans -= a[i]
print(ans)

# Examples
#
# Input
# 5 3
# -6 0 35 -2 4
#
# Output
# 8
#
# Input
# 4 2
# 7 0 0 -7
#
# Output
# 7
