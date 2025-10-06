def count_rhombi(w, h):
    total = 0
    for dx in range(1, w // 2 + 1):
        for dy in range(1, h // 2 + 1):
            total += (w - 2 * dx + 1) * (h - 2 * dy + 1)
    return total

# Input
w, h = map(int, input().split())
print(count_rhombi(w, h))


# Examples
#
# Input
# 2 2
#
# Output
# 1
#
# Input
# 1 2
#
# Output
# 0