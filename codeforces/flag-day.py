import sys


def solve():
    # Fast input reading
    try:
        # Read n and m
        line = sys.stdin.readline().split()
        if not line:
            return
        n, m = map(int, line)
    except EOFError:
        return
    except Exception:
        # Handle cases where input reading fails unexpectedly
        return

    # Read all m dances
    dances = []
    for _ in range(m):
        try:
            dancers = list(map(int, sys.stdin.readline().split()))
            dances.append(dancers)
        except EOFError:
            break
        except Exception:
            # Handle incomplete input
            break

    # Initialize a list to store the color for each dancer (1-based index)
    # 0 means uncolored. 1=White, 2=Red, 3=Blue.
    # We use size n+1 so index i corresponds to dancer i.
    dancer_colors = [0] * (n + 1)

    # The set of all possible colors
    ALL_COLORS = {1, 2, 3}

    # Process each dance
    for dance in dances:
        # Dancers a, b, c are 1-based indices
        a, b, c = dance

        # Get the current colors of the three dancers (0 if uncolored)
        color_a = dancer_colors[a]
        color_b = dancer_colors[b]
        color_c = dancer_colors[c]

        # Collect the colors that are already assigned to dancers in this group
        used_colors = set()
        uncolored_dancers = []

        if color_a != 0:
            used_colors.add(color_a)
        else:
            uncolored_dancers.append(a)

        if color_b != 0:
            used_colors.add(color_b)
        else:
            uncolored_dancers.append(b)

        if color_c != 0:
            used_colors.add(color_c)
        else:
            uncolored_dancers.append(c)

        # Determine the colors that need to be assigned to the uncolored dancers
        missing_colors = sorted(list(ALL_COLORS - used_colors))

        # Greedily assign the missing colors to the uncolored dancers
        # The number of missing colors must equal the number of uncolored dancers
        # because a solution is guaranteed and each dance must have all 3 colors.
        # This is essentially distributing the colors one by one.
        for i in range(len(uncolored_dancers)):
            dancer_id = uncolored_dancers[i]
            color_to_assign = missing_colors[i]
            dancer_colors[dancer_id] = color_to_assign

    # The result is the list of colors for dancers 1 through n
    # We slice the list from index 1 to n (exclusive of n+1)
    result = dancer_colors[1:]

    # Print the result as space-separated integers
    print(*(result))


if __name__ == "__main__":
    solve()