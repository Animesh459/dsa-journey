def main():
    n = int(input().strip())
    arr = list(map(int, input().split()))

    total_sum = sum(arr)

    # If total sum is odd, it's impossible
    if total_sum % 2 != 0:
        print(0)
        return

    target = total_sum // 2
    prefix_sum = 0
    count = 0

    # We stop at n-1 to ensure the right part is non-empty
    for i in range(n - 1):
        prefix_sum += arr[i]
        if prefix_sum == target:
            count += 1

    print(count)


if __name__ == "__main__":
    main()

# Examples
#
# Input
# 9
# 1 5 -6 7 9 -16 0 -2 2
#
# Output
# 3
#
# Input
# 3
# 1 1 1
#
# Output
# 0
#
# Input
# 2
# 0 0
#
# Output
# 1
