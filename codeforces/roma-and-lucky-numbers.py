n, k = map(int, input().split())
numbers = list(map(int, input().split()))

def lucky_digit_count(num):
    count = 0
    for digit in str(num):
        if digit in ('4', '7'):
            count += 1
    return count

ans = 0
for num in numbers:
    if lucky_digit_count(num) <= k:
        ans += 1

print(ans)