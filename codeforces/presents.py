n = int(input())
p = list(map(int, input().split()))

result = [0] * n

for i in range(n):
    result[p[i] - 1] = i + 1

print(' '.join(map(str, result)))