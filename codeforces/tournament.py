import sys


def solve():
    """
    Finds the missing game result by identifying the two players
    with N-2 games recorded and determining the winner based on
    their existing win counts.
    """
    try:
        # Read the number of participants from the first line
        N = int(sys.stdin.readline().strip())
    except:
        # Handle empty or invalid N
        return

    # Calculate the total number of games
    total_games = N * (N - 1) // 2
    num_recorded_games = total_games - 1

    # Initialize statistics arrays (1-based indexing)
    # total_games_count[i]: counts total recorded games for participant i (wins + losses)
    total_games_count = [0] * (N + 1)
    # recorded_wins_count[i]: counts recorded wins for participant i
    recorded_wins_count = [0] * (N + 1)

    # Process all recorded game results line by line
    for _ in range(num_recorded_games):
        try:
            line = sys.stdin.readline().strip()
            if not line:
                break

            # Read two numbers from the line
            winner, loser = map(int, line.split())
        except:
            continue

        # Update win count
        recorded_wins_count[winner] += 1

        # Update total games count for both participants
        total_games_count[winner] += 1
        total_games_count[loser] += 1

    # --- Find the missing match opponents ---

    missing_players = []
    expected_games_count = N - 1

    # The two participants in the missing game will have N-2 recorded games
    for i in range(1, N + 1):
        if total_games_count[i] == expected_games_count - 1:
            missing_players.append(i)

    # These are the two players in the missing match
    A = missing_players[0]
    B = missing_players[1]

    # --- Determine the winner of the missing match ---

    wins_A = recorded_wins_count[A]
    wins_B = recorded_wins_count[B]

    # The one with more existing wins is the faster sleeper and must win the missing match.
    if wins_A > wins_B:
        result_winner = A
        result_loser = B
    else:
        result_winner = B
        result_loser = A

    # Output the result: 4 3 for the example
    print(f"{result_winner} {result_loser}")


if __name__ == '__main__':
    # This ensures the function runs when the script is executed
    solve()