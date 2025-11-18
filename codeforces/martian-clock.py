def val(ch):
    return ord(ch) - 48 if '0' <= ch <= '9' else ord(ch) - 55

def strip(s):
    i = 0
    while i + 1 < len(s) and s[i] == '0':
        i += 1
    return s[i:]

def convert(s, base, limit):
    x = 0
    for ch in s:
        d = val(ch)
        if d >= base:
            return None
        x = x * base + d
        if x > limit:
            return x
    return x

a, b = input().split(':')

# maximum digit
mx = 0
for ch in a + b:
    mx = max(mx, val(ch))
start = max(2, mx + 1)

# Check infinite-case:
# After stripping leading zeros, if both become 1 digit and both digits form valid time,
# then the value does NOT depend on base and works for ALL base >= start.
sa = strip(a)
sb = strip(b)
if len(sa) == 1 and len(sb) == 1:
    ha = val(sa)
    mb = val(sb)
    if 0 <= ha <= 23 and 0 <= mb <= 59:
        print(-1)
        exit()

# Otherwise enumerate finite bases.
# We only need to test bases up to 60, because beyond that all multi-digit numbers grow and exceed limits.
valid = []
for base in range(start, 61):
    ha = convert(a, base, 23)
    if ha is None or ha > 23:
        continue
    mb = convert(b, base, 59)
    if mb is None or mb > 59:
        continue
    valid.append(base)

if not valid:
    print(0)
else:
    print(*valid)
