def solve():
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + arr[i]

    best_count = 1
    best_value = arr[0]

    left = 0

    for right in range(n):
        # cost to make all elements in [left, right] equal arr[right]
        window_size = right - left + 1
        target = arr[right]

        current_sum = prefix[right + 1] - prefix[left]
        cost = target * window_size - current_sum

        while cost > k:
            left += 1
            window_size = right - left + 1
            current_sum = prefix[right + 1] - prefix[left]
            cost = target * window_size - current_sum

        if window_size > best_count:
            best_count = window_size
            best_value = target

    print(best_count, best_value)
