def s(x):
    return sum(map(int, str(x)))

def solve():
    n = int(input())
    ans = -1

    for sx in range(1, 163):  # 9 * 18 = 162 for n up to 1e18
        # The equation: x^2 + s(x)*x - n = 0
        # Solve for x: x = (-s(x) + sqrt(s(x)^2 + 4*n)) / 2
        D = sx * sx + 4 * n
        sqrtD = int(D ** 0.5)
        if sqrtD * sqrtD != D:
            continue
        x = (-sx + sqrtD) // 2
        if x > 0 and x * x + s(x) * x == n:
            ans = x
            break

    print(ans)

if __name__ == "__main__":
    solve()
