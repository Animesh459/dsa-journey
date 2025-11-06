import itertools


def solve():
    # Read the input integer n
    try:
        n = int(input())
    except EOFError:
        return
    except ValueError:
        # Handle cases where input might not be a valid integer, although constrained by problem
        return

    # Super lucky numbers must have an equal count of 4s and 7s,
    # meaning the total number of digits must be even.
    # Since n <= 10^9, the largest possible super lucky number we need to check
    # has 10 digits (5 fours and 5 sevens).

    # Store all generated super lucky numbers
    super_lucky_numbers = set()

    # Iterate through possible total lengths (2k) of the super lucky numbers
    # The number of 4s (and 7s) 'k' ranges from 1 to 5.
    for k in range(1, 6):
        # Create the base sequence: k fours and k sevens
        base_digits = ['4'] * k + ['7'] * k

        # Generate all unique permutations of this sequence
        # Using set() around permutations ensures only unique arrangements are processed
        # However, itertools.permutations with duplicates already handles this implicitly
        # when we convert the list of digits to a string, then to an integer, and store in a set.
        for perm in itertools.permutations(base_digits):
            # Join the tuple of characters into a string
            num_str = "".join(perm)

            # Convert to integer and add to the set
            super_lucky_numbers.add(int(num_str))

    # Convert the set to a list and sort the super lucky numbers
    sorted_super_lucky = sorted(list(super_lucky_numbers))

    # Find the least super lucky number which is not less than n
    result = -1
    for lucky_num in sorted_super_lucky:
        if lucky_num >= n:
            result = lucky_num
            break

    # The result should always be found because the maximum n is 10^9
    # and the largest generated number (7777744444) is > 10^9.
    if result != -1:
        print(result)


if __name__ == "__main__":
    solve()