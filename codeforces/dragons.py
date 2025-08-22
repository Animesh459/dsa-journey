def dragons():
    s, n = map(int, input().split())
    dragons = []

    for _ in range(n):
        x, y = map(int, input().split())
        dragons.append((x, y))

    # Sort dragons by their strength
    dragons.sort()

    for x, y in dragons:
        if s > x:
            s += y
        else:
            print("NO")
            return

    print("YES")


# Example usage:
# Input:
# 2 2
# 1 99
# 100 0
#
# Output: YES

if __name__ == "__main__":
    dragons()