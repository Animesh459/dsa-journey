import sys
import math


# Increase recursion limit for safety, though not strictly needed here
# sys.setrecursionlimit(2000)

def solve():
    """
    Reads the input and calculates the minimum number of shots required.
    """
    try:
        # Read n, x0, y0
        line = sys.stdin.readline().split()
        if not line:
            return

        n = int(line[0])
        x0 = int(line[1])
        y0 = int(line[2])
    except EOFError:
        return
    except Exception:
        return

    # A set to store the unique line identifiers (slopes or 'vertical')
    unique_lines = set()

    for _ in range(n):
        try:
            # Read stormtrooper coordinates (xi, yi)
            xi, yi = map(int, sys.stdin.readline().split())
        except EOFError:
            break
        except Exception:
            break

        # Calculate the change in coordinates
        dx = xi - x0
        dy = yi - y0

        # Case 1: Vertical Line (dx is 0)
        if dx == 0:
            # The line is vertical. Use a unique string to represent it.
            unique_lines.add('vertical')

        # Case 2: Non-Vertical Line (dx is not 0)
        else:
            # The slope m = dy / dx uniquely identifies the line.
            # We must use floating-point division to get the correct slope.
            slope = dy / dx
            unique_lines.add(slope)

    # The minimum number of shots is the number of unique lines found.
    print(len(unique_lines))


if __name__ == "__main__":
    solve()