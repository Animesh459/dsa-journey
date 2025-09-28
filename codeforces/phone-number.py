import sys


def solve():
    """
    Reads friend data, classifies phone numbers, calculates maximum counts
    for each type (taxi, pizza, girl), and prints the resulting lists of friends.
    """

    # Use sys.stdin.readline for efficient, line-by-line reading
    # and strip() to remove the newline character and any trailing whitespace.
    def read_line():
        return sys.stdin.readline().strip()

    try:
        # Read the number of friends
        line = read_line()
        if not line:
            return
        n = int(line)
    except Exception:
        return

    # List to store friend data: (name, taxi_count, pizza_count, girl_count)
    friends_data = []

    # Initialize maximum counts to 0
    max_taxi = 0
    max_pizza = 0
    max_girl = 0

    for _ in range(n):
        # Read s_i and name_i
        header = read_line().split()
        if not header:
            # Handle unexpected end of input if n was wrong
            break

        s_i = int(header[0])
        name_i = header[1]

        taxi_count = 0
        pizza_count = 0
        girl_count = 0

        # Read s_i phone numbers
        for _ in range(s_i):
            phone_raw = read_line()

            # Remove hyphens to get a 6-digit string
            phone = phone_raw.replace('-', '')

            # --- Classification Logic ---

            # 1. Taxi: six identical digits (e.g., 22-22-22)
            # Check if all 6 characters are the same as the first character
            if len(set(phone)) == 1:
                taxi_count += 1
                continue

            # 2. Pizza: strictly decreasing sequence of six different digits (e.g., 98-73-21)
            is_pizza = True

            # Must have six different digits
            if len(set(phone)) != 6:
                is_pizza = False
            else:
                # Check for strictly decreasing sequence: d_i > d_{i+1}
                for j in range(5):
                    # Convert to int for proper comparison
                    if int(phone[j]) <= int(phone[j + 1]):
                        is_pizza = False
                        break

            if is_pizza:
                pizza_count += 1
                continue

            # 3. Girls: all other numbers
            girl_count += 1

        # Update maximum counts
        max_taxi = max(max_taxi, taxi_count)
        max_pizza = max(max_pizza, pizza_count)
        max_girl = max(max_girl, girl_count)

        # Store the friend's data
        friends_data.append((name_i, taxi_count, pizza_count, girl_count))

    # --- Determine the friends with the maximum counts ---
    # We include all friends whose count equals the maximum count found.
    best_taxi_friends = [name for name, taxi, _, _ in friends_data if taxi == max_taxi]
    best_pizza_friends = [name for name, _, pizza, _ in friends_data if pizza == max_pizza]
    best_girl_friends = [name for name, _, _, girl in friends_data if girl == max_girl]

    # --- Print the results in the required format ---
    # Use ', '.join(list) to get the comma-space separated list of names.

    # Taxi
    print(f"If you want to call a taxi, you should call: {', '.join(best_taxi_friends)}.")

    # Pizza
    print(f"If you want to order a pizza, you should call: {', '.join(best_pizza_friends)}.")

    # Girls
    print(f"If you want to go to a cafe with a wonderful girl, you should call: {', '.join(best_girl_friends)}.")


if __name__ == "__main__":
    # The program should pass a Codeforces test since it uses sys.stdin.readline
    # which is the preferred method for large inputs in CP environments.
    solve()