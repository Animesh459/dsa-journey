line = input()

# Remove the curly braces and split by comma
elements = line[1:-1].split(", ")

# Use a set to store only unique letters
unique_letters = set()
print(unique_letters)
# Add each non-empty element to the set
for letter in elements:
    if letter:  # this skips empty strings like when input is "{}"
        unique_letters.add(letter)

# Print the count of distinct letters
print(len(unique_letters))

# Input
# {a, b, c}
#
# Output
# 3
#
# Input
# {b, a, b, a}
#
# Output
# 2
#
# Input
# {}
#
# Output
# 0