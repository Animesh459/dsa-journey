def solve():
    import sys
    input = sys.stdin.readline

    n = int(input().strip())
    a = [int(input().strip()) for _ in range(n)]

    # Case 1: all same -> no pour
    if len(set(a)) == 1:
        print("Exemplary pages.")
        return

    s = sorted(a)

    # Expected median
    T = s[n // 2]

    # Find cups not equal to T
    diffs = [(i, a[i]) for i in range(n) if a[i] != T]

    # Must be exactly 2
    if len(diffs) != 2:
        print("Unrecoverable configuration.")
        return

    (i1, v1), (i2, v2) = diffs

    # Identify source and destination
    if v1 < T and v2 > T:
        a_idx, b_idx = i1, i2
    elif v2 < T and v1 > T:
        a_idx, b_idx = i2, i1
    else:
        print("Unrecoverable configuration.")
        return

    v = abs(a[a_idx] - T)

    # Validate
    if a[a_idx] != T - v or a[b_idx] != T + v:
        print("Unrecoverable configuration.")
        return

    print(f"{v} ml. from cup #{a_idx + 1} to cup #{b_idx + 1}.")

if __name__ == "__main__":
    solve()
