def is_lucky(num):
    # A lucky number contains only digits 4 or 7
    return all(ch in '47' for ch in str(num))


def solve():
    n = int(input().strip())

    # Check if n itself is lucky
    if is_lucky(n):
        print("YES")
        return

    # Check if divisible by any lucky number up to 1000
    for i in range(1, n + 1):
        if is_lucky(i) and n % i == 0:
            print("YES")
            return

    print("NO")


# Run the function
solve()