import sys


def main():
    n = int(sys.stdin.readline().strip())
    ans = []

    l, r = 1, n
    while l <= r:
        ans.append(l)
        l += 1
        if l <= r:
            ans.append(r)
            r -= 1

    print(*ans)


if __name__ == "__main__":
    main()
