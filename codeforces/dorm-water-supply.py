def solve():
    n, p = map(int, input().split())

    outgoing = [None] * (n + 1)
    indeg = [0] * (n + 1)
    outdeg = [0] * (n + 1)

    for _ in range(p):
        a, b, d = map(int, input().split())
        outgoing[a] = (b, d)
        outdeg[a] += 1
        indeg[b] += 1

    res = []

    for i in range(1, n + 1):
        # tank: has outgoing but no incoming
        if outdeg[i] == 1 and indeg[i] == 0:
            cur = i
            min_diam = 10**18

            while outgoing[cur] is not None:
                nxt, diam = outgoing[cur]
                min_diam = min(min_diam, diam)
                cur = nxt

            res.append((i, cur, min_diam))

    print(len(res))
    for a, b, d in res:
        print(a, b, d)


if __name__ == "__main__":
    solve()


Examples
InputCopy
3 2
1 2 10
2 3 20
OutputCopy
1
1 3 10
InputCopy
3 3
1 2 20
2 3 10
3 1 5
OutputCopy
0
InputCopy
4 2
1 2 60
3 4 50
OutputCopy
2
1 2 60
3 4 50
