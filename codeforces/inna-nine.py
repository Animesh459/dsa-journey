def solve():
    import sys
    a = sys.stdin.readline().strip()
    n = len(a)

    ans = 1
    m = 0  # count consecutive pairs summing to 9

    for i in range(n - 1):
        if int(a[i]) + int(a[i + 1]) == 9:
            m += 1
        else:
            if m > 0:
                ans *= (m + 2) // 2
                m = 0

    if m > 0:  # last segment
        ans *= (m + 2) // 2

    print(ans)

if __name__ == "__main__":
    solve()