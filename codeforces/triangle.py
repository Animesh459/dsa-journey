def main():
    a, b = map(int, input().split())

    # Special impossible case
    if a == 1 and b == 1:
        print("NO")
        return

    x1, y1 = 0, 0
    x2, y2 = a, b
    x3, y3 = -b, a

    print("YES")
    print(x1, y1)
    print(x2, y2)
    print(x3, y3)

if __name__ == "__main__":
    main()


# Examples
# Input
# 1 1

# Output
# NO

# Input
# 5 5

# Output
# YES
# 2 1
# 5 5
# -2 4

# Input
# 5 10

# Output
# YES
# -10 4
# -2 -2
# 1 2
