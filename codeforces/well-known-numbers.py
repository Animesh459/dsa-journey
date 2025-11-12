def solve():
    s, k = map(int, input().split())

    # Generate k-bonacci numbers up to > s
    seq = [0] * (k - 1) + [1]
    while seq[-1] <= s:
        seq.append(sum(seq[-k:]))

    # Remove duplicates (only one 0)
    uniq = []
    for x in seq:
        if not uniq or uniq[-1] != x:
            uniq.append(x)

    # Greedy selection from largest to smallest
    res = []
    for x in reversed(uniq):
        if x <= s:
            s -= x
            res.append(x)
        if s == 0:
            break

    # Ensure at least two distinct numbers
    if len(res) == 1:
        res.append(0)

    print(len(res))
    print(*res)


if __name__ == "__main__":
    solve()
