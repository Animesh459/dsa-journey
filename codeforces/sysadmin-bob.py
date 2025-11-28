def main():
    s = input().strip()
    n = len(s)

    at = [i for i, ch in enumerate(s) if ch == '@']
    k = len(at)

    if k == 0:
        print("No solution")
        return

    # First email cannot start with '@'
    if at[0] == 0:
        print("No solution")
        return

    # Check spacing constraints
    for i in range(k - 1):
        # Need distance >=2 => ensures B >=1 and next A >=1
        if at[i + 1] - at[i] < 3:
            print("No solution")
            return

    # Last email must have B>=1
    if at[-1] == n - 1:
        print("No solution")
        return

    result = []
    start = 0

    # Build all emails except last
    for i in range(k - 1):
        end = at[i + 1] - 1  # last char of this email
        result.append(s[start:end])
        start = end

    # Last email: goes to end
    result.append(s[start:])

    print(",".join(result))


if __name__ == "__main__":
    main()
