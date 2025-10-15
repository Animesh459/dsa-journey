MOD = 1000000007

x, y = map(int, input().split())
n = int(input())

# sequence pattern of length 6
seq = [x, y, y - x, -x, -y, x - y]

# find index (adjust because list is 0-indexed)
result = seq[(n - 1) % 6] % MOD

print(result)
