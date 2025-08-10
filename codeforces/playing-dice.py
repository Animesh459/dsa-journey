a, b = map(int, input().split())

first_win = 0
draw = 0
second_win = 0

for dice in range(1, 7):
    diff_a = abs(a - dice)
    diff_b = abs(b - dice)

    if diff_a < diff_b:
        first_win += 1
    elif diff_a > diff_b:
        second_win += 1
    else:
        draw += 1

print(first_win, draw, second_win)
