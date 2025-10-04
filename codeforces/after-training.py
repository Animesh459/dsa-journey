import heapq
import math
import sys


# Set a higher recursion limit for safety, though this solution is iterative.
# sys.setrecursionlimit(200000)

def solve_simple_io():
    """
    Simulates the ball-sorting process using a min-heap,
    relying on standard input() and print().
    """
    try:
        # Read n and m from the first line of input
        # Note: This is simpler but can be slower than reading the whole stream.
        try:
            n, m = map(int, sys.stdin.readline().split())
        except ValueError:
            # Fallback for empty line or incorrect format
            return
    except Exception:
        return

    # 1. Pre-calculate the middle position for Rule 2
    # Baskets are 1-indexed, so the midpoint is (m + 1) / 2.
    mid_pos = (m + 1) / 2.0

    # 2. Initialize the Priority Queue (Min-Heap)
    # Element format: (ball_count, distance_to_middle, basket_num)
    pq = []
    for i in range(1, m + 1):
        basket_num = i
        # The distance calculation is the second priority
        distance = abs(basket_num - mid_pos)

        # Initial state: 0 balls in every basket
        heapq.heappush(pq, (0, distance, basket_num))

    # 3. Process n balls
    results = []
    for _ in range(n):
        # Pop the best basket (O(log m))
        ball_count, distance, chosen_basket_num = heapq.heappop(pq)

        # Record the result
        results.append(str(chosen_basket_num))

        # Update and push back (O(log m))
        new_ball_count = ball_count + 1
        heapq.heappush(pq, (new_ball_count, distance, chosen_basket_num))

    # Print all results, separated by newlines
    print('\n'.join(results))


if __name__ == "__main__":
    solve_simple_io()