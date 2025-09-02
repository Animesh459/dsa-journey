n = int(input())
a = list(map(int, input().split()))

used = [False] * 3002

for x in a:
    used[x] = True

for i in range(1, 3002):
    if not used[i]:
        print(i)
        break