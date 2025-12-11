def solve():
    n, p = map(int, input().split())
    s = list(input().strip())

    # Convert to 0-based index
    p -= 1

    # Mirror cursor to left side if it is on the right half
    mid = n // 2
    if p >= mid:
        p = n - p - 1

    total_change_cost = 0
    leftmost = n
    rightmost = -1

    # Check mismatches only on left half
    for i in range(mid):
        j = n - i - 1
        if s[i] != s[j]:
            diff = abs(ord(s[i]) - ord(s[j]))
            total_change_cost += min(diff, 26 - diff)
            leftmost = min(leftmost, i)
            rightmost = max(rightmost, i)

    # If no mismatches, no cursor movement needed
    if total_change_cost == 0:
        print(0)
        return

    # Minimal cursor movement to cover all mismatch positions
    move_cost = min(abs(p - leftmost), abs(p - rightmost)) + (rightmost - leftmost)

    print(total_change_cost + move_cost)

if __name__ == "__main__":
    solve()
