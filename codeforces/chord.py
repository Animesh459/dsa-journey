import sys
from itertools import permutations


def main():
    """
    Main function to read input and solve the chord classification problem.
    """
    notes = {
        "C": 0, "C#": 1, "D": 2, "D#": 3, "E": 4, "F": 5,
        "F#": 6, "G": 7, "G#": 8, "A": 9, "B": 10, "H": 11
    }

    try:
        input_line = sys.stdin.readline().strip().split()
        if not input_line:
            return

        input_notes = [notes[note] for note in input_line]

        is_major = False
        is_minor = False

        for p in permutations(input_notes):
            n1, n2, n3 = p

            dist1 = (n2 - n1 + 12) % 12
            dist2 = (n3 - n2 + 12) % 12

            if dist1 == 4 and dist2 == 3:
                is_major = True
                break

            if dist1 == 3 and dist2 == 4:
                is_minor = True
                break

        if is_major:
            print("major")
        elif is_minor:
            print("minor")
        else:
            print("strange")

    except Exception as e:
        # For competitive programming, this is often not needed
        # but can be useful for debugging
        # print(f"An error occurred: {e}", file=sys.stderr)
        pass


if __name__ == "__main__":
    main()