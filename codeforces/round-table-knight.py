n = int(input().strip())
moods = list(map(int, input().split()))

for k in range(1, n):
    if n % k != 0:
        continue

    # polygon must have at least 3 vertices
    if n // k < 3:
        continue

    for start in range(k):
        good = True
        for i in range(start, n, k):
            if moods[i] == 0:
                good = False
                break
        if good:
            print("YES")
            exit()

print("NO")
