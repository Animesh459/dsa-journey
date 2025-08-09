# Read input
n, k, l, c, d, p, nl, np = map(int, input().split())

total_drink = k * l
toasts_by_drink = total_drink // nl
toasts_by_limes = c * d
toasts_by_salt = p // np

result = min(toasts_by_drink, toasts_by_limes, toasts_by_salt) // n
print(result)
