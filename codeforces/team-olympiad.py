n = int(input())
skills = list(map(int, input().split()))

programmers = []
mathematicians = []
athletes = []

# Step 1: Separate children by their skills
for i in range(n):
    if skills[i] == 1:
        programmers.append(i + 1)
    elif skills[i] == 2:
        mathematicians.append(i + 1)
    elif skills[i] == 3:
        athletes.append(i + 1)

# Step 2: Find max number of teams
w = min(len(programmers), len(mathematicians), len(athletes))
print(w)

# Step 3: Form teams
for i in range(w):
    print(programmers[i], mathematicians[i], athletes[i])
