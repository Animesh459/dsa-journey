def solve():
    s = input().strip()
    res = []

    for c in s:
        res.append(c)
        ln = len(res)

        # Rule 1: No three identical letters
        if ln >= 3 and res[ln-1] == res[ln-2] == res[ln-3]:
            res.pop()
            continue

        # Rule 2: No pattern AABB
        if ln >= 4 and res[ln-4] == res[ln-3] and res[ln-2] == res[ln-1]:
            res.pop()

    print("".join(res))


if __name__ == "__main__":
    solve()
