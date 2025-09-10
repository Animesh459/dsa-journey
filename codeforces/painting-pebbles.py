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