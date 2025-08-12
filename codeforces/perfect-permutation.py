n = int(input())

if n % 2 != 0:
    print(-1)
else:
    result = []
    for i in range(1, n + 1, 2):
        result.append(i + 1)
        result.append(i)
    print(*result)