def main():
    import sys
    input = sys.stdin.readline

    n = int(input().strip())
    a = list(map(int, input().split()))

    ans = set()
    cur = set()

    for val in a:
        new_cur = {val}
        for x in cur:
            new_cur.add(x | val)
        cur = new_cur
        ans.update(cur)

    print(len(ans))


if __name__ == "__main__":
    main()


# Examples
# InputCopy
# 3
# 1 2 0
# OutputCopy
# 4
# InputCopy
# 10
# 1 2 3 4 5 6 1 2 9 10
# OutputCopy
# 11