from math import floor

x, y, n = map(int, input().split())

best_a, best_b = 0, 1
best_diff = abs(x * 1 - y * 0)  # arbitrary start, will be overwritten

for b in range(1, n + 1):
    a = (x * b) // y  # floor of x*b/y
    for candidate_a in (a, a + 1):  # check both floor and ceil candidates
        diff = abs(candidate_a * y - x * b)
        # Compare scaled differences: diff/y*b, but avoid floats
        if (diff * best_b < best_diff * b or
            (diff * best_b == best_diff * b and (b < best_b or (b == best_b and candidate_a < best_a)))):
            best_a, best_b, best_diff = candidate_a, b, diff

print(f"{best_a}/{best_b}")
