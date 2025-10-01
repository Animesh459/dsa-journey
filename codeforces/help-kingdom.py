import sys
import io


# Set up standard input to allow reading the whole input as a string.
# While not strictly necessary for a single line of input, it's good practice
# for competitive programming to handle I/O cleanly.
# The following two lines are generally only needed when running in a local environment
# that doesn't correctly handle I/O streaming, but they don't hurt.
# sys.stdin = io.StringIO(input_data)
# input = sys.stdin.readline

def solve():
    """
    Reads the number, formats it into the financial format, and prints the result.
    """
    try:
        # Read the entire input as a single line string
        number_str = sys.stdin.readline().strip()
    except EOFError:
        # Handle case where input is empty
        return

    # 1. Determine the sign and remove it from the string
    is_negative = number_str.startswith('-')
    if is_negative:
        # Remove the leading minus sign
        number_str = number_str[1:]

    # 2. Separate the integer and fractional parts
    if '.' in number_str:
        integer_part, fractional_part = number_str.split('.', 1)
    else:
        integer_part = number_str
        fractional_part = ""

    # Ensure integer_part is not empty (it shouldn't be based on problem constraints,
    # but good for robustness if the number was ".123"). Since the problem guarantees
    # "at least one decimal digit", this is mainly for numbers like ".5" which aren't
    # allowed by the rule "The decimal point (if it is present) is unique and is preceded
    # and followed by a non-zero quantity on decimal digits."
    if not integer_part:
        integer_part = "0"

    # 3. Format the fractional part (two digits, truncation, zero padding)
    # The fractional part must contain exactly two digits.

    # Take the first two digits (truncating any extra)
    formatted_fractional = fractional_part[:2]

    # Pad with zeros if necessary
    if len(formatted_fractional) < 2:
        formatted_fractional = formatted_fractional.ljust(2, '0')

    # 4. Format the integer part (grouping with commas)
    # The groups are of three digits, starting from the least significant ones (right to left).

    formatted_integer = []
    # Iterate over the integer part string backwards
    for i in range(len(integer_part) - 1, -1, -1):
        # Append the digit
        formatted_integer.append(integer_part[i])

        # Add a comma after every third digit, unless it's the very last digit being processed
        # (which corresponds to the most significant digit in the original number).
        # We add the comma if we've processed 3 digits AND we haven't reached the start.
        # The index from the right is (len(integer_part) - 1) - i
        digits_from_right = len(integer_part) - 1 - i

        if (digits_from_right + 1) % 3 == 0 and i != 0:
            formatted_integer.append(',')

    # The list is built in reverse order, so reverse it and join to form the string
    formatted_integer_part = "".join(reversed(formatted_integer))

    # 5. Assemble the final financial number string

    # Combine integer and fractional parts with a decimal point
    financial_number = f"{formatted_integer_part}.{formatted_fractional}"

    # 6. Apply currency sign and brackets

    # Currency sign
    currency_sign = "$"

    if is_negative:
        # For negative numbers: "($...)"
        final_result = f"({currency_sign}{financial_number})"
    else:
        # For non-negative numbers: "$..."
        final_result = f"{currency_sign}{financial_number}"

    # Print the final result
    print(final_result)


# Call the solve function to run the logic
solve()