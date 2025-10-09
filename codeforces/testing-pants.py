import sys


def solve():
    """
    Calculates the worst-case number of clicks required to pass the test.

    The total worst-case clicks T is the sum of the clicks needed to successfully
    pass each question (Q_i) for the first time, starting from the moment Q_i is reached.

    For question i (1-based index) with a_i variants:
    1. Worst case requires (a_i - 1) wrong attempts before the correct answer is found.
    2. Each wrong attempt at Q_i causes a reset to Q_1.
    3. The recovery from Q_1 back to Q_i requires (i - 1) clicks (since the correct
       answers for Q_1 to Q_{i-1} are remembered, they take 1 click each).
    4. Total clicks per failure cycle: 1 (wrong click at Q_i) + (i - 1) (recovery clicks) = i clicks.
    5. Clicks for (a_i - 1) failures: (a_i - 1) * i
    6. The final successful click at Q_i costs 1 click.
    7. Total clicks to pass Q_i (when reached successfully) = (a_i - 1) * i + 1

    T = sum_{i=1 to n} (a_i - 1) * i + 1
    """
    try:
        # Read the number of questions, n
        n_line = sys.stdin.readline()
        if not n_line:
            # Handle empty input
            return
        n = int(n_line.strip())

        # Read the number of variants for each question, a_i
        a_line = sys.stdin.readline()
        if not a_line:
            if n > 0:
                # n was read, but a_i was not, return 0 if n=0, otherwise something is wrong.
                return
            else:
                # n=0, total clicks is 0
                print(0)
                return

        # Map the input string to a list of integers
        a = list(map(int, a_line.split()))

    except Exception:
        # General error handling for bad input format
        return

    # Total clicks must be stored in a variable capable of holding large numbers
    # (up to ~10^13, which Python's standard integers handle automatically)
    total_clicks = 0

    # Iterate through the questions. i represents the 0-based index.
    for i in range(n):
        # a_i is the number of variants for the current question
        a_i = a[i]

        # question_num is the 1-based index of the question (i + 1)
        question_num = i + 1

        # Clicks for Q_i = (a_i - 1) * question_num + 1
        # This is the cost incurred during the sequence of attempts (failures + final success)
        # required to pass the current question for the first time.
        clicks_for_q_i = (a_i - 1) * question_num + 1

        total_clicks += clicks_for_q_i

    print(total_clicks)


if __name__ == "__main__":
    solve()
