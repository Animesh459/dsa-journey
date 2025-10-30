v = int(input())
a = list(map(int, input().split()))

# Find the minimum cost and its corresponding digit
min_cost = min(a)
min_digit = a.index(min_cost) + 1  # because digits are 1-based

# Maximum possible length of the number
length = v // min_cost
if length == 0:
    print(-1)
    exit()

remaining = v
ans = []

# Build the number
for i in range(length):
    # Try to place the largest possible digit at this position
    for d in range(9, 0, -1):
        cost = a[d - 1]
        # Check if after placing this digit, we can still fill the rest with the cheapest one
        if remaining - cost >= (length - i - 1) * min_cost and remaining >= cost:
            ans.append(str(d))
            remaining -= cost
            break

print("".join(ans))
