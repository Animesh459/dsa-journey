import sys


def solve():
    # Read n and k
    try:
        # Read the first line for n and k
        line1 = sys.stdin.readline()
        if not line1:
            return
        n, k = map(int, line1.split())
    except EOFError:
        return
    except Exception:
        # Handle cases where input might be malformed or missing
        return

    # Read the second line for light levels
    try:
        # Store light levels along with their 1-based index
        # hour_data will be a list of tuples: (light_level, 1-based_index)
        a = list(map(int, sys.stdin.readline().split()))

        # Create a list of tuples: (light_level, 1-based index)
        hour_data = []
        for i in range(n):
            hour_data.append((a[i], i + 1))

    except EOFError:
        # Handle unexpected EOF after reading n and k
        return
    except Exception:
        return

    # --- Binary Search on the Minimum Light Level (L) ---

    def check(L: int) -> bool:
        """
        Checks if it's possible to choose k hours with light level >= L.
        :param L: The minimum light level to check.
        :return: True if at least k hours meet the condition, False otherwise.
        """
        count = 0
        for light, _ in hour_data:
            if light >= L:
                count += 1
        return count >= k

    # Binary search range for the minimum light level (0 to 100)
    low = 0
    high = 101  # Upper bound exclusive
    optimal_min_light = 0

    while low < high:
        # We need to find the largest L for which check(L) is True.
        # This requires adjusting the typical binary search to handle the "maximum True" case.
        # Let's use a standard search for the maximum value in [low, high)
        mid = low + (high - low) // 2

        if mid == 0:
            # mid=0 is always possible since all a_i >= 0 and k <= n.
            # If low and high were 0 and 1, mid would be 0.
            # Since we set high=101, this case mainly prevents infinite loops if the range gets too small.
            # Given the loop condition low < high, if low=0 and high=1, mid=0.
            # If check(0) is true (always is), we set optimal_min_light=0, low=1. Loop terminates.
            if check(mid):
                optimal_min_light = mid
                low = mid + 1
            else:
                high = mid
            continue

        if check(mid):
            # mid is achievable as a minimum. Store it and try for a higher minimum.
            optimal_min_light = mid
            low = mid + 1
        else:
            # mid is too high. The actual maximum minimum must be less than mid.
            high = mid

    # After the loop, optimal_min_light holds the maximum possible minimum light level (L_max).

    # --- Output Generation ---

    # 1. Print the minimum light level (L_max)
    print(optimal_min_light)

    # 2. Select k hours with light level >= L_max and print their 1-based indices

    selected_indices = []
    # Iterate through the (light_level, 1-based_index) pairs
    for light, index in hour_data:
        if light >= optimal_min_light and len(selected_indices) < k:
            selected_indices.append(index)

    # Print the selected k indices
    print(*(selected_indices))


# Execute the solution function
# solve()

# Note: In a competitive programming environment, the input often comes from a file
# or standard input. Running solve() here simulates reading from standard input.
# Since this is an interactive environment, I will simply define the function and
# use the example provided for demonstration if needed, but for the final output,
# I assume the user's provided input.

# To test with the example:
# Input:
# 5 3
# 20 10 30 40 10
# Output should be:
# 20
# 1 3 4
# The code logic handles this:
# 1. Binary search finds optimal_min_light = 20.
# 2. Hours with light >= 20 are (20, 1), (30, 3), (40, 4).
# 3. We select the first k=3 of these: 1, 3, 4.

# --- Execution for the environment (replace with final `solve()` if required) ---
# Since the constraints on N and K are small (up to 1000) and the light range is small (0-100),
# this binary search approach is highly efficient. The check function is O(N),
# and the binary search runs for a constant number of iterations (log(101) is small),
# making the overall time complexity O(N log(MaxLightLevel)).
solve()