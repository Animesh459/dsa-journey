import sys

def solve():
    """
    Reads laptop data, sorts it by price, and checks if quality is non-monotonic.
    """
    try:
        n = int(sys.stdin.readline())
        laptops = []
        for _ in range(n):
            a, b = map(int, sys.stdin.readline().split())
            laptops.append((a, b))

        # Sort the laptops based on their price
        laptops.sort()

        # Check if there is any pair where price increases but quality decreases
        is_alex_happy = False
        for i in range(n - 1):
            if laptops[i][1] > laptops[i+1][1]:
                is_alex_happy = True
                break

        if is_alex_happy:
            print("Happy Alex")
        else:
            print("Poor Alex")

    except (IOError, ValueError):
        # Handle potential errors with input
        return

if __name__ == "__main__":
    solve()