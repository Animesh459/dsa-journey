# Days in each month of 2013 (non-leap year)
mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Prefix sum of days for month to convert date to day index
prefix = [0] * 13
for m in range(1, 13):
    prefix[m] = prefix[m - 1] + mdays[m]

def date_to_day(m, d):
    return prefix[m - 1] + (d - 1)  # 0-based day index

n = int(input())
ops = []
min_day = 10**9
max_day = -10**9

for _ in range(n):
    m, d, p, t = map(int, input().split())
    olympiad_day = date_to_day(m, d)
    start = olympiad_day - t      # preparation starts
    end = olympiad_day - 1        # preparation ends
    ops.append((start, end, p))
    min_day = min(min_day, start)
    max_day = max(max_day, end)

# Shift days to make array indices non-negative
shift = -min_day
size = max_day - min_day + 5
diff = [0] * size

# Build difference array
for s, e, p in ops:
    s += shift
    e += shift
    diff[s] += p
    diff[e + 1] -= p

# Compute prefix sum and find maximum concurrent jury
cur = 0
ans = 0
for x in diff:
    cur += x
    ans = max(ans, cur)

print(ans)
