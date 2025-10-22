def longest_fib_segment(n, a):
    if n <= 2:
        return n  # Any segment of length 1 or 2 is always good

    max_len = 2
    current_len = 2

    for i in range(2, n):
        if a[i] == a[i - 1] + a[i - 2]:
            current_len += 1
        else:
            current_len = 2  # reset because this breaks the Fibonacci property
        max_len = max(max_len, current_len)

    return max_len


# Input handling
n = int(input())
a = list(map(int, input().split()))
print(longest_fib_segment(n, a))
