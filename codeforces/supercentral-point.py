# Read the number of points from the first line of input.
try:
    n = int(input())
except (EOFError, ValueError):
    n = 0

# Create an empty list to store the coordinates of all points.
points = []

# Read the coordinates for each point and store them as tuples in the list.
for _ in range(n):
    try:
        x, y = map(int, input().split())
        points.append((x, y))
    except (EOFError, ValueError):
        # Stop reading if there are no more valid points.
        break

# Initialize a counter for the number of supercentral points found.
supercentral_count = 0

# Iterate through each point in the list to check if it is supercentral.
for i in range(n):
    x_i, y_i = points[i]

    # Initialize boolean flags to track the presence of neighbors in each direction.
    has_left = False
    has_right = False
    has_lower = False
    has_upper = False

    # Iterate through all other points to find neighbors for the current point.
    for j in range(n):
        # Skip the point itself.
        if i == j:
            continue

        x_j, y_j = points[j]

        # Check for neighbors on the same horizontal line.
        if y_j == y_i:
            if x_j < x_i:
                has_left = True
            elif x_j > x_i:
                has_right = True

        # Check for neighbors on the same vertical line.
        if x_j == x_i:
            if y_j < y_i:
                has_lower = True
            elif y_j > y_i:
                has_upper = True

    # If the point has at least one neighbor in all four directions, it is supercentral.
    if has_left and has_right and has_lower and has_upper:
        supercentral_count += 1

# Print the final count of supercentral points.
print(supercentral_count)
