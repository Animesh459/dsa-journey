import math


def main():
    r, x, y, x2, y2 = map(int, input().split())

    # Calculate the distance between centers
    distance = math.hypot(x2 - x, y2 - y)

    # Each move shifts the center by 2*r
    steps = math.ceil(distance / (2 * r))

    print(steps)


if __name__ == "__main__":
    main()
