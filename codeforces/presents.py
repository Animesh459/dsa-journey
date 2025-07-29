n = int(input())
p = list(map(int, input().split()))
print('n', n)
print('p', p)
result = [0] * n
print('result', result)
for i in range(n):
    result[p[i] - 1] = i + 1

print(' '.join(map(str, result)))