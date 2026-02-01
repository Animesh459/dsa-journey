import sys
from itertools import permutations

def solve():
    s = sys.stdin.readline().strip()

    digits = list(s)

    for d in "1689":
        digits.remove(d)

    zeros = digits.count('0')
    non_zero = [d for d in digits if d != '0']
    non_zero.sort()

    if not non_zero:
        base = ""
        base_mod = 0
    else:
        first = non_zero[0]
        rest = non_zero[1:]
        base = first + '0' * zeros + ''.join(rest)

        base_mod = 0
        for c in base:
            base_mod = (base_mod * 10 + int(c)) % 7

    for p in permutations("1689"):
        cur = base_mod
        for d in p:
            cur = (cur * 10 + int(d)) % 7

        if cur == 0:
            print(base + ''.join(p) + ('0' * zeros if not non_zero else ""))
            return

    print(0)

if __name__ == "__main__":
    solve()


# Examples
# InputCopy
# 1689
# OutputCopy
# 1869
# InputCopy
# 18906
# OutputCopy
# 18690
