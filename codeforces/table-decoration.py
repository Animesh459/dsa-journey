# Codeforces console I/O

r, g, b = map(int, input().split())
a, b, c = sorted([r, g, b])

if c > a + b:
    # Largest pile dominates
    print(a + b)
else:
    # Balanced enough to use total // 3
    print((a + b + c) // 3)
