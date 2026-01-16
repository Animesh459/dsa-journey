MOD = 1000000009

def solve():
    n, m, k = map(int, input().split())

    w = n - m
    safe = (w + 1) * (k - 1)

    if m <= safe:
        print(m % MOD)
        return

    block_size = m - safe
    t = block_size // k

    score = (pow(2, t + 1, MOD) - 2) % MOD
    score = (score * k) % MOD
    score = (score + (m - t * k)) % MOD

    print(score)


solve()

#
# Examples
#
# Input
# 5 3 2
#
# Output
# 3
#
# Input
# 5 4 2
#
# Output
# 6
