import sys

def main():
    s = sys.stdin.readline().strip()
    a, b = map(int, sys.stdin.readline().split())
    n = len(s)

    # prefix_mod[i] = value of s[0..i] % a
    prefix_mod = [0] * n
    cur = 0
    for i in range(n):
        cur = (cur * 10 + (ord(s[i]) - 48)) % a
        prefix_mod[i] = cur

    # suffix_mod[i] = value of s[i..n-1] % b
    suffix_mod = [0] * n
    cur = 0
    power10 = 1
    for i in range(n - 1, -1, -1):
        digit = ord(s[i]) - 48
        cur = (digit * power10 + cur) % b
        suffix_mod[i] = cur
        power10 = (power10 * 10) % b

    for i in range(n - 1):
        if prefix_mod[i] == 0 and suffix_mod[i + 1] == 0:
            # Check no leading zeros on right
            if s[i + 1] != '0':
                print("YES")
                print(s[:i + 1])
                print(s[i + 1:])
                return

    print("NO")


if __name__ == "__main__":
    main()
