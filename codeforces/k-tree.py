MOD = 1000000007

def solve():
    n, k, d = map(int, input().split())

    # DP for using weights 1..k
    f = [0] * (n + 1)
    f[0] = 1
    for s in range(1, n + 1):
        for w in range(1, k + 1):
            if s - w >= 0:
                f[s] = (f[s] + f[s - w]) % MOD

    # DP for using weights 1..(d-1)
    g = [0] * (n + 1)
    g[0] = 1
    for s in range(1, n + 1):
        for w in range(1, d):
            if s - w >= 0:
                g[s] = (g[s] + g[s - w]) % MOD

    # Result = all paths - paths without any edge >= d
    ans = (f[n] - g[n]) % MOD
    print(ans)


if __name__ == "__main__":
    solve()
