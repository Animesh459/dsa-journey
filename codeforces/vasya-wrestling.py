n = int(input())
a = [int(input()) for _ in range(n)]

first = []
second = []
sum_first = 0
sum_second = 0

for x in a:
    if x > 0:
        first.append(x)
        sum_first += x
    else:
        second.append(-x)
        sum_second += -x

# Determine winner
if sum_first > sum_second:
    print("first")
elif sum_second > sum_first:
    print("second")
else:
    # Compare lexicographically
    if first > second:
        print("first")
    elif second > first:
        print("second")
    else:
        # If sequences are same, check who performed last
        if a[-1] > 0:
            print("first")
        else:
            print("second")
