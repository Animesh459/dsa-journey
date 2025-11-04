import sys


def solve():
    # Reading input for table A
    try:
        # Read na and ma, handling potential EOF
        line = sys.stdin.readline()
        if not line:
            return
        na, ma = map(int, line.split())
    except EOFError:
        return
    except ValueError:
        return

    A = []
    # Read table A rows
    for _ in range(na):
        row_str = sys.stdin.readline().strip()
        # Convert '0'/'1' characters to integers 0/1
        A.append([int(c) for c in row_str])

    # Reading input for table B
    try:
        # Read nb and mb
        line = sys.stdin.readline()
        if not line:
            return
        nb, mb = map(int, line.split())
    except EOFError:
        return
    except ValueError:
        return

    B = []
    # Read table B rows
    for _ in range(nb):
        row_str = sys.stdin.readline().strip()
        B.append([int(c) for c in row_str])

    # Initialize maximum overlap found so far and the best shift
    max_overlap = -1
    best_shift = (0, 0)

    # Determine the search range for shifts (x, y)
    # The shift x must be such that:
    # 1. i + x >= 1  => x >= 1 - i. Min i is 1 (x >= 0). Max i is na (x >= 1 - na). Overall: x >= 1 - na
    # 2. i + x <= nb => x <= nb - i. Max i is 1 (x <= nb - 1). Min i is na (x <= nb - na). Overall: x <= nb - 1
    # Range for x: [1 - na, nb - 1]
    # Range for y: [1 - ma, mb - 1]

    # Iterate over all possible row shifts (x)
    # Note: The problem uses 1-based indexing in the formula, but our lists use 0-based indexing.
    # The loops below use 0-based indices i_a and j_a for table A.
    # The mapping is: i = i_a + 1, j = j_a + 1
    # The indices for B are: i_b = (i_a + 1) + x - 1 = i_a + x
    #                      j_b = (j_a + 1) + y - 1 = j_a + y

    # We iterate i_a from 0 to na-1, j_a from 0 to ma-1
    # The index for B is i_b = i_a + x and j_b = j_a + y
    # Conditions for B: 0 <= i_a + x < nb  and  0 <= j_a + y < mb

    min_x = 1 - na
    max_x = nb - 1
    min_y = 1 - ma
    max_y = mb - 1

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            current_overlap = 0

            # Iterate over all cells of table A (0-based)
            for i_a in range(na):
                for j_a in range(ma):
                    # Check if the cell A[i_a][j_a] is '1'
                    if A[i_a][j_a] == 1:
                        # Calculate corresponding indices in table B
                        i_b = i_a + x
                        j_b = j_a + y

                        # Check if the corresponding cell in B is within bounds
                        if 0 <= i_b < nb and 0 <= j_b < mb:
                            # Check if the cell B[i_b][j_b] is also '1'
                            if B[i_b][j_b] == 1:
                                current_overlap += 1

            # Update the maximum overlap and the best shift
            if current_overlap > max_overlap:
                max_overlap = current_overlap
                best_shift = (x, y)

    # The problem asks for the *shift* (x, y), not the overlap factor.
    print(f"{best_shift[0]} {best_shift[1]}")


solve()