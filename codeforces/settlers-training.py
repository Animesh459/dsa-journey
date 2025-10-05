import sys


def solve():
    """
    Simulates the training process to find the number of golden coins (training sessions)
    needed to raise all soldiers to rank k.
    """
    try:
        # Read n and k
        # We use sys.stdin.readline for robust input reading
        line1 = sys.stdin.readline().split()
        if not line1:
            return
        n = int(line1[0])
        k = int(line1[1])

        # Read the initial ranks (a_i)
        ranks_initial = list(map(int, sys.stdin.readline().split()))
    except:
        return

    # A frequency list to store the count of soldiers at each rank.
    # ranks_count[r] will store the number of soldiers at rank r (1-based rank).
    # Since k <= 100, a list of size k+1 is sufficient (index 0 unused, 1 to k used).
    ranks_count = [0] * (k + 1)

    # Populate the initial counts
    for rank in ranks_initial:
        ranks_count[rank] += 1

    # The total number of golden coins/training sessions
    coins = 0

    # The simulation runs until all soldiers are at rank k.
    # The total number of soldiers is n.
    while ranks_count[k] < n:
        # Increment the coin count (start of a new training session)
        coins += 1

        # We need to process ranks from 1 up to k-1.
        # This is because promotion happens from rank i to i+1.

        # In a single session, promotions must be calculated based on the
        # ranks *at the start* of the session. We use a list to track
        # how many soldiers move *into* the next rank.
        promoted_into_next_rank = [0] * (k + 1)

        # Loop from rank 1 up to k-1
        for current_rank in range(1, k):

            # Check Rule: The group must be below rank k (which is true for current_rank < k)
            # and there must be at least one soldier in the group.
            count = ranks_count[current_rank]

            if count > 0:
                # Rule: Exactly one soldier increases rank by one.

                # 1. Decrease count at the current rank
                ranks_count[current_rank] -= 1

                # 2. Mark a soldier to be added to the next rank (current_rank + 1)
                promoted_into_next_rank[current_rank + 1] += 1

        # After calculating all promotions based on the starting ranks,
        # apply the new counts.
        for rank_to_update in range(2, k + 1):
            ranks_count[rank_to_update] += promoted_into_next_rank[rank_to_update]

    # Output the total number of sessions (coins)
    print(coins)


if __name__ == "__main__":
    solve()


#
# Examples
#
# Input
# 4 4
# 1 2 2 3
#
# Output
# 4
#
# Input
# 4 3
# 1 1 1 1
#
# Output
# 5
