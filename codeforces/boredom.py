

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

MAX = 100000
freq = [0] * (MAX + 1)

# Count frequency of each value
for x in arr:
    freq[x] += 1

# DP over values:
# dp[i] = max points using values up to i
dp = [0] * (MAX + 1)

dp[1] = freq[1] * 1

for i in range(2, MAX + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + freq[i] * i)

print(dp[MAX])
