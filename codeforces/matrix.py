def solve():
    import sys
    input = sys.stdin.readline

    a = int(input().strip())
    s = input().strip()
    n = len(s)
    digits = [int(c) for c in s]

    # Maximum possible subarray sum = 9 * 4000 = 36000
    MAX_SUM = 9 * n
    cnt = [0] * (MAX_SUM + 1)

    # Count all subarray sums
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += digits[j]
            cnt[curr_sum] += 1

    total_intervals = n * (n + 1) // 2

    if a == 0:
        z = cnt[0]
        # R = 0 or C = 0
        answer = 2 * z * total_intervals - z * z
        print(answer)
        return

    answer = 0
    d = 1
    while d * d <= a:
        if a % d == 0:
            e = a // d
            if d <= MAX_SUM and e <= MAX_SUM:
                if d == e:
                    answer += cnt[d] * cnt[e]
                else:
                    answer += cnt[d] * cnt[e]
                    answer += cnt[e] * cnt[d]
        d += 1

    print(answer)

solve()