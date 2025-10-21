def george_and_round():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    i = j = 0  # pointers for a and b

    while i < n and j < m:
        if b[j] >= a[i]:
            i += 1  # this b[j] can cover a[i]
        j += 1

    print(n - i)  # remaining unmatched required problems


george_and_round()
