n, v = map(int, input().split())
sellers = []

for i in range(1, n + 1):
    items = list(map(int, input().split()))
    k, prices = items[0], items[1:]
    # check if Valera can outbid any item
    if any(price < v for price in prices):
        sellers.append(i)

print(len(sellers))
if sellers:
    print(" ".join(map(str, sellers)))