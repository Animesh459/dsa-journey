p, d = map(int, input().split())

best = p  # start with original price
for i in range(18):  # up to 10^18, so at most 18 digits
    pow10 = 10 ** i
    # candidate: reduce p to something ending with all 9s from current position
    candidate = (p // pow10) * pow10 - 1
    if candidate < 0:
        continue
    if p - candidate <= d:
        best = candidate
    else:
        break

print(best)
