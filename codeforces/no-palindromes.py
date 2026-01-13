def is_valid(s, i):
    # Check palindrome of length 2
    if i > 0 and s[i] == s[i - 1]:
        return False
    # Check palindrome of length 3
    if i > 1 and s[i] == s[i - 2]:
        return False
    return True


def next_tolerable(n, p, s):
    s = list(s)

    # Try to modify from right to left
    for i in range(n - 1, -1, -1):
        for c in range(ord(s[i]) + 1, ord('a') + p):
            s[i] = chr(c)

            # Check if valid up to i
            if not is_valid(s, i):
                continue

            ok = True
            for j in range(i + 1, n):
                placed = False
                for x in range(ord('a'), ord('a') + p):
                    s[j] = chr(x)
                    if is_valid(s, j):
                        placed = True
                        break
                if not placed:
                    ok = False
                    break

            if ok:
                return "".join(s)

    return "NO"


if __name__ == "__main__":
    n, p = map(int, input().split())
    s = input().strip()
    print(next_tolerable(n, p, s))

