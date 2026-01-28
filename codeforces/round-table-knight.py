n = int(input().strip())
moods = list(map(int, input().split()))

for k in range(1, n):
    if n % k != 0:
        continue

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


# Examples

# Input
# 3
# 1 1 1

# Output
# YES

# Input
# 6
# 1 0 1 1 1 0

# Output
# YES

# Input
# 6
# 1 0 0 1 0 1

# Output
# NO
