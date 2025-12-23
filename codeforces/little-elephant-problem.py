import sys


def solve():
    line1 = sys.stdin.readline()
    if not line1:
        return
    n = int(line1.strip())

    a = []
    while len(a) < n:
        line = sys.stdin.readline()
        if not line:
            break
        a.extend(map(int, line.split()))

    sorted_a = sorted(a)
    diff_count = 0
    for i in range(n):
        if a[i] != sorted_a[i]:
            diff_count += 1

    if diff_count <= 2:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    solve()