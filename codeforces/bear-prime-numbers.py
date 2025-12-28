import sys

input = sys.stdin.readline


def main():
    n = int(input())
    arr = list(map(int, input().split()))

    MAXV = max(arr)

    # Count frequency of each number
    cnt = [0] * (MAXV + 1)
    for x in arr:
        cnt[x] += 1

    # Sieve of Eratosthenes
    is_prime = bytearray(b'\x01') * (MAXV + 1)
    is_prime[0] = is_prime[1] = 0

    # f[p] = count of numbers divisible by p
    f = [0] * (MAXV + 1)

    for i in range(2, MAXV + 1):
        if is_prime[i]:
            for j in range(i, MAXV + 1, i):
                f[i] += cnt[j]
                if j > i:
                    is_prime[j] = 0

    # Prefix sum over primes
    pref = [0] * (MAXV + 1)
    for i in range(2, MAXV + 1):
        pref[i] = pref[i - 1]
        if is_prime[i]:
            pref[i] += f[i]

    m = int(input())
    out = []

    for _ in range(m):
        l, r = map(int, input().split())
        if l > MAXV:
            out.append("0")
        else:
            r = min(r, MAXV)
            out.append(str(pref[r] - pref[l - 1]))

    print("\n".join(out))


if __name__ == "__main__":
    main()
