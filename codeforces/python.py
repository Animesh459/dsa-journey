import math

# Read the number of circles
n = int(input())

# Read the radii as a list of integers
radii = list(map(int, input().split()))

# Sort the radii in descending order
radii.sort(reverse=True)

# Calculate the total red area
total_red_area_sum = 0
for i, r in enumerate(radii):
    if i % 2 == 0:
        # Add the area of the current circle
        total_red_area_sum += r**2
    else:
        # Subtract the area of the current circle
        total_red_area_sum -= r**2

# Multiply the final sum of squares by pi
total_red_area = total_red_area_sum * math.pi

# Print the result with the required precision
print(f"{total_red_area:.10f}")