import math

a, b, c, d = map(int, input().split())

# We compare the ratios a/b (screen) and c/d (movie)
if a * d > b * c:
    # The movie will fit by height, leaving empty space horizontally
    # Scale by height: movie height = screen height
    p = a * d - b * c
    q = a * d
else:
    # The movie will fit by width, leaving empty space vertically
    # Scale by width: movie width = screen width
    p = b * c - a * d
    q = b * c

# Simplify fraction p/q
g = math.gcd(p, q)
p //= g
q //= g

print(f"{p}/{q}")
