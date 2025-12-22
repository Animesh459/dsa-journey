import sys

def main():
    n, k, d = map(int, sys.stdin.readline().split())

    # Check if k^d >= n (without overflow)
    total = 1
    for _ in range(d):
        total *= k
        if total >= n:
            break

    if total < n:
        print(-1)
        return

    # ans[day][student]
    ans = [[0] * n for _ in range(d)]

    for student in range(n):
        x = student
        for day in range(d):
            ans[day][student] = (x % k) + 1
            x //= k

    for day in range(d):
        print(*ans[day])


if __name__ == "__main__":
    main()
