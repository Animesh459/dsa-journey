MOD = 10**9 + 7

def main():
    n, m = map(int, input().split())
    pos = list(map(int, input().split()))
    pos.sort()

    # Precompute factorials and inverse factorials
    fact = [1] * (n + 1)
    invfact = [1] * (n + 1)

    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD

    invfact[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n, 0, -1):
        invfact[i - 1] = invfact[i] * i % MOD

    gaps = []

    # Left gap
    gaps.append(pos[0] - 1)

    # Middle gaps
    middle_gaps = []
    for i in range(m - 1):
        gap = pos[i + 1] - pos[i] - 1
        gaps.append(gap)
        middle_gaps.append(gap)

    # Right gap
    gaps.append(n - pos[-1])

    off = n - m
    ans = fact[off]

    # Divide by factorial of each gap
    for g in gaps:
        ans = ans * invfact[g] % MOD

    # Multiply by 2^(gap-1) for middle gaps
    for g in middle_gaps:
        if g > 0:
            ans = ans * pow(2, g - 1, MOD) % MOD

    print(ans)


if __name__ == "__main__":
    main()


Examples
InputCopy
3 1
1
OutputCopy
1
InputCopy
4 2
1 4
OutputCopy
2
InputCopy
11 2
4 8
OutputCopy
6720