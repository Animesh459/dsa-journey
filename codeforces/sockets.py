n, m, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
sockets = k
devices_to_plug = m
filters_used = 0
if sockets >= devices_to_plug:
    print(0)
else:
    for i in range(n):
        sockets = sockets - 1 + a[i]
        filters_used += 1
        if sockets >= devices_to_plug:
            print(filters_used)
            break
    else:
        print(-1)