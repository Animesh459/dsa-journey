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
