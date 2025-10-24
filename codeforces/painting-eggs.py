n = int(input())
diff = 0  # Sa - Sg
res = []

for _ in range(n):
    a, g = map(int, input().split())
    # Try giving the egg to A if it keeps |diff| within 500
    if diff + a <= 500:
        res.append('A')
        diff += a
    else:
        res.append('G')
        diff -= g  # since a + g = 1000, g = 1000 - a

if abs(diff) <= 500:
    print(''.join(res))
else:
    print(-1)
