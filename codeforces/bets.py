import sys


def solve():
    """
    Calculates the maximum possible profit by betting on the winner of each section.
    """
    # Fast input reading
    try:
        # Read n (number of sections) and m (number of participants)
        line = sys.stdin.readline().split()
        if not line:
            return
        n = int(line[0])
        m = int(line[1])
    except EOFError:
        return
    except Exception:
        return

    # Read participant data
    # Store as a list of tuples: (l_i, r_i, t_i, c_i)
    # The index in the list will be the participant number (1-based)
    participants = []
    for _ in range(m):
        try:
            l, r, t, c = map(int, sys.stdin.readline().split())
            participants.append((l, r, t, c))
        except EOFError:
            break
        except Exception:
            break

    # Total maximum profit
    total_profit = 0

    # Iterate through each section k from 1 to n
    for k in range(1, n + 1):
        # Initialize winner variables for section k
        # We need to track the winner's time (min_time), index (winner_idx), and profit (winner_profit)

        # Initialize with values that ensure the first valid participant becomes the winner
        min_time = float('inf')
        winner_idx = float('inf')  # Track the 1-based index (i+1)
        winner_profit = 0

        # Iterate through all m participants (0-based index i)
        for i in range(m):
            # i_actual is the 1-based participant number
            i_actual = i + 1

            # Extract participant data
            l_i, r_i, t_i, c_i = participants[i]

            # Check if participant i runs section k (l_i <= k <= r_i)
            if l_i <= k <= r_i:
                # Check for winner conditions:

                # 1. New minimum time
                if t_i < min_time:
                    min_time = t_i
                    winner_idx = i_actual
                    winner_profit = c_i

                # 2. Tie in time, but smaller index wins
                elif t_i == min_time:
                    if i_actual < winner_idx:
                        # This case is redundant if we update min_time only if the index is smaller,
                        # but keeping it clear: if times are equal, the smaller index wins.
                        min_time = t_i  # Already the same, but for clarity
                        winner_idx = i_actual
                        winner_profit = c_i

        # After checking all participants, if a winner was found (winner_idx is not inf), 
        # add the profit to the total.
        if winner_idx != float('inf'):
            total_profit += winner_profit

    # Print the final result
    print(total_profit)


# Call the solve function
solve()