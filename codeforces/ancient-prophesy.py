import collections


def solve():

    try:
        prophesy = input()
    except EOFError:
        return

    # A date string is 10 characters long: "DD-MM-YYYY"
    DATE_LENGTH = 10

    # Stores the count of each valid date found
    date_counts = collections.defaultdict(int)

    # 1. Iterate through all possible starting positions for a date substring
    for i in range(len(prophesy) - DATE_LENGTH + 1):
        substring = prophesy[i: i + DATE_LENGTH]

        # 2. Check for the "dd-mm-yyyy" format
        # Check lengths and the position of hyphens
        if (len(substring) != DATE_LENGTH or
                substring[2] != '-' or
                substring[5] != '-'):
            continue

        # Check if characters at other positions are digits
        is_valid_format = True
        for j in [0, 1, 3, 4, 6, 7, 8, 9]:
            if not substring[j].isdigit():
                is_valid_format = False
                break

        if not is_valid_format:
            continue

        # 3. Extract Day, Month, Year
        day_str = substring[0:2]
        month_str = substring[3:5]
        year_str = substring[6:10]

        try:
            day = int(day_str)
            month = int(month_str)
            year = int(year_str)
        except ValueError:
            # Should not happen if the previous check passed, but good practice
            continue

        # 4. Check date validity constraints

        # A. Year constraint
        if not (2013 <= year <= 2015):
            continue

        # B. Month constraint
        if not (1 <= month <= 12):
            continue

        # C. Day constraint (Strictly more than a zero)
        if day <= 0:
            continue

        # D. Maximum days in the month constraint (for non-leap years)
        max_days = 0

        # Months with 31 days
        if month in [1, 3, 5, 7, 8, 10, 12]:
            max_days = 31
        # Months with 30 days
        elif month in [4, 6, 9, 11]:
            max_days = 30
        # February (28 days since 2013-2015 are not leap years)
        elif month == 2:
            max_days = 28

        if day > max_days:
            continue

        # 5. The date is valid, count its occurrence
        date_counts[substring] += 1

    # 6. Find the date with the maximum count
    # The problem guarantees that such a date exists and is unique.
    apocalypse_date = ""
    max_count = -1

    for date, count in date_counts.items():
        if count > max_count:
            max_count = count
            apocalypse_date = date

    print(apocalypse_date)


if __name__ == "__main__":
    solve()