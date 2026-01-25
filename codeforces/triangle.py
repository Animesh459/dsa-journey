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
