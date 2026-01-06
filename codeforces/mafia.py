import math


def main():
    n = int(input().strip())
    a = list(map(int, input().split()))

    total_needed = sum(a)
    max_needed = max(a)

    rounds_by_total = math.ceil(total_needed / (n - 1))

    print(max(max_needed, rounds_by_total))


if __name__ == "__main__":
    main()
