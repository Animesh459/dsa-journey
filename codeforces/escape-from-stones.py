import sys
from collections import deque

def main():
    s = sys.stdin.readline().strip()
    n = len(s)

    dq = deque()

    # Process stones from last to first
    for i in range(n - 1, -1, -1):
        stone_number = i + 1
        if s[i] == 'l':
            dq.append(stone_number)
        else:  # 'r'
            dq.appendleft(stone_number)

    # Output result
    out = sys.stdout.write
    for x in dq:
        out(str(x) + "\n")

if __name__ == "__main__":
    main()
