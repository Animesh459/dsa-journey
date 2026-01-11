def rational_resistance(a, b):
    ans = 0
    while b != 0:
        ans += a // b
        a, b = b, a % b
    return ans


def solve():
    a, b = map(int, input().split())
    print(rational_resistance(a, b))


if __name__ == "__main__":
    solve()
