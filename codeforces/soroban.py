import sys

def main():
    pos = int(sys.stdin.readline())
    for _ in range(3):
        a, b = map(int, sys.stdin.readline().split())
        if pos == a:
            pos = b
        elif pos == b:
            pos = a
    print(pos)

if __name__ == "__main__":
    main()