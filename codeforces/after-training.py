import math

def solve():
    """
    Reads n and m, and simulates the process of placing n balls into m baskets
    according to Valeric's scheme.
    """
    try:
        # Read n and m
        line = input().split()
        if not line:
            return
        n = int(line[0])
        m = int(line[1])
    except EOFError:
        return
    except Exception:
        return

    # A list to store the number of balls in each basket.
    # basket_counts[i] will store the count for basket i+1 (0-indexed to 1-indexed).
    basket_counts = [0] * m

    # The ideal middle position is (m + 1) / 2.
    # We use float for accurate distance calculation.
    mid_pos = (m + 1) / 2.0

    # Process each of the n balls
    results = []
    for _ in range(n):
        # 1. Find the minimum number of balls currently in any basket.
        min_balls = min(basket_counts)

        # Initialize the chosen basket index and its metrics for comparison.
        # chosen_basket_index