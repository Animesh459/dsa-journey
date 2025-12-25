def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    ra = find(parent, a)
    rb = find(parent, b)
    if ra != rb:
        parent[rb] = ra


def main():
    n = int(input())
    points = []

    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    parent = list(range(n))

    for i in range(n):
        for j in range(i + 1, n):
            if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
                union(parent, i, j)

    components = set(find(parent, i) for i in range(n))
    print(len(components) - 1)


if __name__ == "__main__":
    main()
