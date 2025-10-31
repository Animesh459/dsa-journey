def lowbit(x):
    return x & -x


def main():
    sum_value, limit = map(int, input().split())
    nums = [(lowbit(i), i) for i in range(1, limit + 1)]
    nums.sort(reverse=True)  # sort by lowbit descending

    result = []
    current_sum = 0

    for lb, num in nums:
        if current_sum + lb <= sum_value:
            current_sum += lb
            result.append(num)
        if current_sum == sum_value:
            break

    if current_sum == sum_value:
        print(len(result))
        print(*result)
    else:
        print(-1)


if __name__ == "__main__":
    main()
