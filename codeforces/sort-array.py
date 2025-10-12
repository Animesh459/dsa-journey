n = int(input())
a = list(map(int, input().split()))

sorted_a = sorted(a)

# find the first and last mismatch
l, r = 0, 0
for i in range(n):
    if a[i] != sorted_a[i]:
        l = i
        break

for i in range(n - 1, -1, -1):
    if a[i] != sorted_a[i]:
        r = i
        break

# If already sorted
if a == sorted_a:
    print("yes")
    print(1, 1)
else:
    # Reverse the segment
    a[l:r+1] = a[l:r+1][::-1]
    if a == sorted_a:
        print("yes")
        print(l + 1, r + 1)
    else:
        print("no")
