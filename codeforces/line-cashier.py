# A. Line to Cashier

n = int(input())
k = list(map(int, input().split()))

ans = float('inf')
for i in range(n):
    items = list(map(int, input().split()))
    time_i = 5 * sum(items) + 15 * len(items)
    ans = min(ans, time_i)

print(ans)