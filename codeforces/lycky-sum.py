import bisect

def generate_lucky(limit=10**9):
    lucky = []

    def dfs(num):
        if num > limit:
            return
        if num > 0:
            lucky.append(num)
        dfs(num * 10 + 4)
        dfs(num * 10 + 7)

    dfs(0)
    lucky.sort()
    return lucky

def main():
    l, r = map(int, input().split())

    lucky_numbers = generate_lucky()

    cur = l
    ans = 0

    while cur <= r:
        idx = bisect.bisect_left(lucky_numbers, cur)
        nxt = lucky_numbers[idx]

        # numbers from cur to min(r, nxt) will have next(x) = nxt
        end = min(r, nxt)
        count = end - cur + 1

        ans += nxt * count
        cur = end + 1

    print(ans)

main()

#
# Examples
# InputCopy
# 2 7
# OutputCopy
# 33
# InputCopy
# 7 7
# OutputCopy
# 7