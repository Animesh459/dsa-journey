import sys

MOD = 1000000007

def main():
    data = sys.stdin.read().strip().split()
    n, m = map(int, data[:2])
    names = data[2:]

    answer = 1
    for col in range(m):
        distinct_chars = set()
        for row in range(n):
            distinct_chars.add(names[row][col])
        answer = (answer * len(distinct_chars)) % MOD

    print(answer)

if __name__ == "__main__":
    main()
