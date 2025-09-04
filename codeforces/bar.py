n = int(input())
alcoholic_drinks = [
    "ABSINTH", "BEER", "BRANDY", "CHAMPAGNE", "GIN", "RUM", "SAKE",
    "TEQUILA", "VODKA", "WHISKEY", "WINE"
]
count = 0
for _ in range(n):
    s = input()
    if s.isdigit():
        age = int(s)
        if age < 18:
            count += 1
    else:
        if s in alcoholic_drinks:
            count += 1
print(count)