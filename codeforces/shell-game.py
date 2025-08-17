def solve():
    """
    This function solves the Shell Game problem.
    """

    # Read the initial position of the ball (1-indexed)
    try:
        pos = int(input())
    except (IOError, ValueError):
        # Handle potential empty input or non-integer input
        return

    # Process the three shuffles
    for _ in range(3):
        try:
            # Read the two cups being shuffled
            a, b = map(int, input().split())

            # Update the ball's position if it's one of the cups being swapped
            if pos == a:
                pos = b
            elif pos == b:
                pos = a
        except (IOError, ValueError):
            # Handle cases with malformed or missing lines
            # For this specific problem, this shouldn't happen, but it's good practice.
            return

    # Print the final position of the ball
    print(pos)

# Call the solve function to run the logic
solve()