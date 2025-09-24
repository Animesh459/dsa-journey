import sys

def solve():
    """
    Calculates the probability of SmallR winning the archer match.
    """
    try:
        a, b, c, d = map(int, sys.stdin.readline().split())
    except (IOError, ValueError):
        return

    # Probability of SmallR hitting the target
    p = a / b

    # Probability of Zanoes hitting the target
    q = c / d

    # Probability of both missing in a single round (one shot by each)
    # The common ratio of the geometric series
    common_ratio = (1 - p) * (1 - q)

    # Sum of the infinite geometric series: S = A / (1 - R)
    # where A = p (SmallR's first-turn win probability)
    # and R = common_ratio
    if common_ratio == 1:
        # This case happens if p=0 and q=0. No one ever hits. SmallR wins with 0 probability.
        # This prevents a division by zero error, though the formula holds
        # if we consider the limit as the denominator approaches 0.
        # But given the problem constraints, it's safer to handle explicitly.
        # If both p and q are 0, no one ever wins, and since SmallR
        # can't win, the probability is 0.
        print(0.0)
    else:
        probability_smallr_wins = p / (1 - common_ratio)
        print(f"{probability_smallr_wins:.12f}")

if __name__ == "__main__":
    solve()