n = int(input().strip())

count = 0
queue = ["1"]

while queue:
    s = queue.pop(0)
    value = int(s)

    if value > n:
        continue

    count += 1
    queue.append(s + "0")
    queue.append(s + "1")

print(count)
