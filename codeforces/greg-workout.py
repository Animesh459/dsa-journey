n = int(input())
exercises = list(map(int, input().split()))

chest_sum = 0
biceps_sum = 0
back_sum = 0

for i in range(n):
    if (i + 1) % 3 == 1:
        chest_sum += exercises[i]
    elif (i + 1) % 3 == 2:
        biceps_sum += exercises[i]
    else:
        back_sum += exercises[i]

if chest_sum > biceps_sum and chest_sum > back_sum:
    print("chest")
elif biceps_sum > chest_sum and biceps_sum > back_sum:
    print("biceps")
else:
    print("back")