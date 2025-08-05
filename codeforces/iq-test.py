n = int(input())
numbers = list(map(int, input().split()))

even_indices = []
odd_indices = []

for i in range(n):
    if numbers[i] % 2 == 0:
        even_indices.append(i + 1)  # +1 because positions start from 1
    else:
        odd_indices.append(i + 1)

# The one with only one element is the different one
if len(even_indices) == 1:
    print(even_indices[0])
else:
    print(odd_indices[0])
