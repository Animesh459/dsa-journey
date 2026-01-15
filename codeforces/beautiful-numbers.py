MOD = 1000000007

def is_good(x, a, b):
    s = str(x)
    for c in s:
        if c != str(a) and c != str(b):
            return False
    return True

def modpow(a, b):
    res = 1
    while b > 0:
        if b & 1:
            res = res * a % MOD
        a = a * a % MOD
        b >>= 1
    return res

def solve():
    a, b, n = map(int, input().split())

    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD

    invfact = [1] * (n + 1)
    invfact[n] = modpow(fact[n], MOD - 2)
    for i in range(n, 0, -1):
        invfact[i - 1] = invfact[i] * i % MOD

    def comb(n, k):
        return fact[n] * invfact[k] % MOD * invfact[n - k] % MOD

    ans = 0
    for k in range(n + 1):
        s = a * (n - k) + b * k
        if is_good(s, a, b):
            ans = (ans + comb(n, k)) % MOD

    print(ans)


if __name__ == "__main__":
    solve()

Examples
Input
1 3 3
Output
1
Input
2 3 10
Output
165
