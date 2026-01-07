import sys
input = sys.stdin.readline

n = int(input())
# We maintain:
# values: the actual appended values
# add: additional increments applied to each position
values = [0]  # initial sequence has one element: 0
add = [0]
total_sum = 0.0  # keep running sum as float

for _ in range(n):
    op = input().split()
    t = int(op[0])

    if t == 1:
        a, x = int(op[1]), int(op[2])
        # apply x to first a elements, specifically increase add[a-1]
        total_sum += a * x
        add[a - 1] += x

    elif t == 2:
        k = int(op[1])
        values.append(k)
        add.append(0)
        total_sum += k

    else:  # t == 3
        # remove last element
        if len(values) > 1:
            last_value = values.pop()
            last_add = add.pop()
            total_sum -= last_value + last_add
            add[-1] += last_add  # propagate removed add to previous element

    # print current average
    print(total_sum / len(values))


# Examples
#
# Input
# 5
# 2 1
# 3
# 2 3
# 2 1
# 3
#
# Output
# 0.500000
# 0.000000
# 1.500000
# 1.333333
# 1.500000
#
# Input
# 6
# 2 1
# 1 2 20
# 2 2
# 1 2 -3
# 3
# 3
#
# Output
# 0.500000
# 20.500000
# 14.333333
# 12.333333
# 17.500000
# 17.000000