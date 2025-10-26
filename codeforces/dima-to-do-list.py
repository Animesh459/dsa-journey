import sys


def solve():
    # Read n and k
    try:
        # Read n and k from the first line
        line = sys.stdin.readline().split()
        if not line:
            return
        n, k = map(int, line)
    except EOFError:
        return
    except Exception:
        return

    # Read the powers a_i
    try:
        a = list(map(int, sys.stdin.readline().split()))
    except EOFError:
        return
    except Exception:
        return

    # Check for valid input lengths
    if len(a) != n:
        # Handle case where power list doesn't match n (shouldn't happen with valid input)
        return

    # Initialize a list to store the total telling-off power for each 'group'
    # There are k possible groups, indexed by the remainder (i-1) % k, from 0 to k-1.
    # Group r corresponds to starting task s = r + 1.
    group_sums = [0] * k

    # Iterate through all tasks
    for i in range(n):
        # The task number is i + 1 (1-based index)
        # The corresponding power is a[i]

        # Calculate the remainder: (task_number - 1) % k.
        # This remainder determines the group.
        remainder = i % k

        # Add the power a[i] to the sum of its group
        group_sums[remainder] += a[i]

    # Find the minimum sum and the smallest index (remainder) that achieves it.
    min_sum = float('inf')
    best_remainder = -1

    for r in range(k):
        current_sum = group_sums[r]

        # We look for the minimum sum. If sums are equal, we keep the smaller index (r).
        if current_sum < min_sum:
            min_sum = current_sum
            best_remainder = r

    # The optimal starting task is the smallest task number s such that (s - 1) % k = best_remainder.
    # This task number is best_remainder + 1.
    optimal_start_task = best_remainder + 1

    # Print the result
    print(optimal_start_task)


# Call the solve function
solve()