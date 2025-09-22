def solve():
    """
    Calculates the maximum possible total area of a garland.

    This function reads two strings representing available paper sheets and
    required garland pieces. It then determines the maximum total area of
    the garland that can be made, by counting the availability of each
    color and the requirement for each color.

    The total area is the sum of the minimum of available sheets and required
    pieces for each color.

    Returns:
        int: The maximum total area of the garland, or -1 if the garland
             cannot be made.
    """
    from collections import Counter

    available_sheets_str = input()
    required_pieces_str = input()

    available_sheets_count = Counter(available_sheets_str)
    required_pieces_count = Counter(required_pieces_str)

    total_area = 0
    for color, required_count in required_pieces_count.items():
        if color not in available_sheets_count:
            print(-1)
            return

        available_count = available_sheets_count[color]
        total_area += min(available_count, required_count)

    print(total_area)


if __name__ == "__main__":
    solve()