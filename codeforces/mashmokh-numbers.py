def solve():
    n, k = map(int, input().split())

    pairs = n // 2

    # Special case: n = 1
    if n == 1:
        if k == 0:
            print(1)
        else:
            print(-1)
        return

    # If we need more points than pairs, or if we need fewer points than pairs (since min gcd is 1)
    if k < pairs:
        print(-1)
        return

    # If k == pairs, all pairs must have gcd = 1
    if k == pairs:
        result = list(range(1, n + 1))
        print(*result)
        return

    first_gcd = k - pairs + 1
    result = [first_gcd, 2 * first_gcd]

    # Add remaining numbers to make pairs with gcd = 1
    current = 1
    while len(result) < n:
        if current != first_gcd and current != 2 * first_gcd:
            result.append(current)
        current += 2  # Use odd numbers

    print(*result)


solve()