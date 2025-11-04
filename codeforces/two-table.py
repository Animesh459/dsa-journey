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