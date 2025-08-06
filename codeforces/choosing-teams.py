n, k = map(int, input().split())
participations = list(map(int, input().split()))

# A student is eligible if they can participate at least k more times
eligible_students = 0

for p in participations:
    if p + k <= 5:
        eligible_students += 1

# Each team needs 3 students
max_teams = eligible_students // 3

print(max_teams)
