def extract_name(token):
    # Remove "'s" from names like "fatma's"
    if token.endswith("'s"):
        return token[:-2]
    return token


def main():
    you = input().strip()
    n = int(input().strip())

    priority = {}
    names = set()

    for _ in range(n):
        line = input().strip().split()

        # X = line[0]
        X = line[0]

        # Determine action
        if line[1] == "posted":
            points = 15
            # Y is before "'s", located at index 3: on Y's wall
            Y = extract_name(line[3])
        elif line[1] == "commented":
            points = 10
            # commented on Y's post → Y is at index 3
            Y = extract_name(line[3])
        else:
            # likes Y's post → Y is at index 2
            points = 5
            Y = extract_name(line[2])

        names.add(X)
        names.add(Y)

        # Only add priority if you are involved
        if X == you or Y == you:
            other = Y if X == you else X
            priority[other] = priority.get(other, 0) + points

    # Remove yourself from list
    if you in names:
        names.remove(you)

    # Ensure everyone appears even if zero priority
    for name in names:
        priority.setdefault(name, 0)

    # Sorting: by (-priority, name)
    sorted_names = sorted(names, key=lambda x: (-priority[x], x))

    # Output
    for name in sorted_names:
        print(name)


if __name__ == "__main__":
    main()
