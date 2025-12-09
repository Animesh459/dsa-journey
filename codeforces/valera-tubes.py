n, m, k = map(int, input().split())

# Step 1: Generate the snake-like traversal of all cells
cells = []
for i in range(1, n + 1):
    if i % 2 == 1:
        for j in range(1, m + 1):
            cells.append((i, j))
    else:
        for j in range(m, 0, -1):
            cells.append((i, j))

# Step 2: Split into k tubes
tube_sizes = [2] * (k - 1)  # first k-1 tubes get 2 cells each
tube_sizes.append(len(cells) - 2 * (k - 1))  # last tube gets the remaining cells

# Step 3: Print the tubes
index = 0
for size in tube_sizes:
    tube = cells[index:index + size]
    print(size, end=' ')
    for x, y in tube:
        print(x, y, end=' ')
    print()
    index += size
