from collections import Counter

def main():
    n = int(input())
    digits = list(map(int, input().split()))
    count = Counter(digits)

    # For divisibility by 2 and 5 → last digit must be 0
    if count[0] == 0:
        print(-1)
        return

    # The sum of digits must be divisible by 3
    total_sum = sum(d * c for d, c in count.items())
    remainder = total_sum % 3

    def remove_digits(rem, cnt):
        """Remove the smallest digits to fix the remainder mod 3."""
        if rem == 0:
            return True
        if rem == 1:
            for d in [1, 4, 7, 2, 5, 8]:
                if count[d] > 0:
                    count[d] -= 1
                    return True
            # Try removing two digits with remainder 2
            removed = 0
            for d in [2, 5, 8]:
                while count[d] > 0 and removed < 2:
                    count[d] -= 1
                    removed += 1
                    if removed == 2:
                        return True
        elif rem == 2:
            for d in [2, 5, 8, 1, 4, 7]:
                if count[d] > 0:
                    count[d] -= 1
                    return True
            # Try removing two digits with remainder 1
            removed = 0
            for d in [1, 4, 7]:
                while count[d] > 0 and removed < 2:
                    count[d] -= 1
                    removed += 1
                    if removed == 2:
                        return True
        return False

    if not remove_digits(remainder, count):
        print(-1)
        return

    # If only zeros remain
    if sum(d * c for d, c in count.items()) == 0:
        print(0)
        return

    # Ensure we have at least one zero for divisibility by 10
    if count[0] == 0:
        print(-1)
        return

    # Construct the number in descending order
    result = ''.join(str(d) * count[d] for d in range(9, -1, -1))
    print(result)


if __name__ == "__main__":
    main()
