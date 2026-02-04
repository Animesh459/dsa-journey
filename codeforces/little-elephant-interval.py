def count_upto(N: int) -> int:
    if N <= 0:
        return 0

    s = str(N)
    L = len(s)
    ans = 0

    # 1-digit numbers
    ans += min(N, 9)

    # Lengths smaller than L
    for length in range(2, L):
        ans += 9 * (10 ** (length - 2))

    # Same length as N
    power = 10 ** (L - 1)
    middle_len = L - 2
    middle_max = 10 ** middle_len if middle_len >= 0 else 1

    for d in range(1, 10):
        base = d * power + d
        if base > N:
            continue

        if middle_len == 0:
            ans += 1
        else:
            max_middle = (N - base) // 10
            ans += max(0, min(max_middle + 1, middle_max))

    return ans


l, r = map(int, input().split())
print(count_upto(r) - count_upto(l - 1))


Examples
InputCopy
2 47
OutputCopy
12
InputCopy
47 1024
OutputCopy
98