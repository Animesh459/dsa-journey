from math import gcd

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if n > m:
    # Degree of numerator > denominator → Infinity or -Infinity
    sign = 1
    if a[0] * b[0] < 0:
        sign = -1
    print("Infinity" if sign > 0 else "-Infinity")

elif n < m:
    # Degree of numerator < denominator → 0
    print("0/1")

else:
    # Degrees are equal → ratio of leading coefficients
    p = a[0]
    q = b[0]
    sign = 1
    if q < 0:
        q = -q
        p = -p
    g = gcd(abs(p), abs(q))
    p //= g
    q //= g
    print(f"{p}/{q}")
