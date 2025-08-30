def solve():
    n = int(input())
    a = list(map(int, input().split()))

    min_overall_difficulty = float('inf')

    # Iterate through each hold from the second to the second-to-last
    # to consider removing it. The first and last holds must stay.
    for i in range(1, n - 1):
        temp_a = a[:i] + a[i + 1:]

        current_difficulty = 0
        for j in range(len(temp_a) - 1):
            current_difficulty = max(current_difficulty, temp_a[j + 1] - temp_a[j])

        min_overall_difficulty = min(min_overall_difficulty, current_difficulty)

    print(min_overall_difficulty)


solve()
#
# Examples
#
# Input
# 3
# 1 4 6
#
# Output
# 5
#
# Input
# 5
# 1 2 3 4 5
#
# Output
# 2
# Input
# 5
# 1 2 3 7 8
#
# Output
# 4