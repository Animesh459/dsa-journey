def main():
    n, m = map(int, input().split())
    res = []
    for x in range(n + 1):
        y1 = m - x
        if 0 <= y1 <= m:
            res.append((x, y1))
    # Shift second half by +1 on y (cyclically)
    for i in range(len(res)):
        if i % 2 == 1 and res[i][1] + 1 <= m:
            res[i] = (res[i][0], res[i][1] + 1)

    print(len(res))
    for x, y in res:
        print(x, y)

if __name__ == "__main__":
    main()
