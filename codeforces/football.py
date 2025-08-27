n = int(input())
team1 = ""
team1_count = 0
team2 = ""
team2_count = 0
for i in range(n):
    goal = input()
    if team1 == "":
        team1 = goal
        team1_count += 1
    elif goal == team1:
        team1_count += 1
    else:
        team2 = goal
        team2_count += 1
if team1_count > team2_count:
    print(team1)
else:
    print(team2)

    # Examples
    #
    # Input
    # 1
    # ABC
    #
    # Output
    # ABC
    #
    # Input
    # 5
    # A
    # ABA
    # ABA
    # A
    # A
    #
    # Output
    # A