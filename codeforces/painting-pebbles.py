n, k = map(int, input().split())
a = list(map(int, input().split()))

min_pebbles = min(a)
max_pebbles = max(a)

if max_pebbles - min_pebbles > k:
    print("NO")
else:
    print("YES")
    for i in range(n):
        colors = []
        for j in range(min_pebbles):
            colors.append(j + 1)
        for j in range(a[i] - min_pebbles):
            colors.append( (j % k) + 1 )
        print(*colors)

#
# Examples
#
# Input
# 4 4
# 1 2 3 4
#
# Output
# YES
#
# 1
# 1 4
# 1 2 4
# 1 2 3 4
#
# Input
# 5 2
# 3 2 4 1 3
#
# Output
# NO
#
# Input
# 5 4
# 3 2 4 3 5
#
# Output
# YES
# 1 2 3
# 1 3
# 1 2 3 4
# 1 3 4
# 1 1 2 3 4