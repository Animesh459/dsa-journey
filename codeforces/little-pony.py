def little_pony_sort_by_shift(n, arr):
    count_breaks = 0
    idx = -1

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            count_breaks += 1
            idx = i  # store the break position

    # If more than one break point, impossible
    if count_breaks > 1:
        return -1

    # If no breaks, already sorted
    if count_breaks == 0:
        return 0

    # Check if rotation actually sorts it
    if arr[-1] > arr[0]:
        return -1

    return n - (idx + 1)


# ---- Input / Output ----
n = int(input())
arr = list(map(int, input().split()))
print(little_pony_sort_by_shift(n, arr))
