import sys

def main():
    s = sys.stdin.readline().strip()
    if not s:
        return
    # Print from last digit to first (least significant to most)
    tails = ["-OOOO", "O-OOO", "OO-OO", "OOO-O", "OOOO-"]
    for ch in reversed(s):
        d = int(ch)
        head = "O-|" if d < 5 else "-O|"
        print(head + tails[d % 5])

if __name__ == "__main__":
    main()
