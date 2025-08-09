# Read input
n, k, l, c, d, p, nl, np = map(int, input().split())

total_drink = k * l
toasts_by_drink = total_drink // nl
toasts_by_limes = c * d
toasts_by_salt = p // np

result = min(toasts_by_drink, toasts_by_limes, toasts_by_salt) // n
print(result)


# Input
# 3 4 5 10 8 100 3 1
#
# Output
# 2
#
# Input
# 5 100 10 1 19 90 4 3
#
# Output
# 3
#
# Input
# 10 1000 1000 25 23 1 50 1
#
# Output
# 0