import sys
import random
import math


def is_prime(n):
    if n < 2:
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def pollards_rho(n):
    if n % 2 == 0:
        return 2
    while True:
        x = random.randrange(2, n - 1)
        y = x
        c = random.randrange(1, n - 1)
        d = 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = math.gcd(abs(x - y), n)
            if d == n:
                break
        if d > 1 and d < n:
            return d


def factor(n, res):
    if n == 1:
        return
    if is_prime(n):
        res.append(n)
    else:
        d = pollards_rho(n)
        factor(d, res)
        factor(n // d, res)



def main():
    q = int(sys.stdin.readline())

    if q == 1:
        print(1)
        print(0)
        return

    if is_prime(q):
        print(1)
        print(0)
        return

    fac = []
    factor(q, fac)

    from collections import Counter
    cnt = Counter(fac)
    primes = list(cnt.keys())

    # Check losing positions
    if len(primes) == 1 and cnt[primes[0]] == 2:
        print(2)
        return

    if len(primes) == 2 and cnt[primes[0]] == 1 and cnt[primes[1]] == 1:
        print(2)
        return

    # Winning position
    print(1)

    # Print a losing divisor
    for p in primes:
        if cnt[p] >= 2:
            print(p * p)
            return

    print(primes[0] * primes[1])


if __name__ == "__main__":
    main()
