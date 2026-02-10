import math

def main():
    k, b, n, t = map(int, input().split())

    # Compute z from the first experiment
    if k == 1:
        z = 1 + n * b
    else:
        z = pow(k, n) + b * (pow(k, n) - 1) // (k - 1)

    # If already enough bacteria
    if t >= z:
        print(0)
        return

    # Second experiment
    if k == 1:
        # Linear growth
        seconds = (z - t + b - 1) // b
        print(seconds)
    else:
        # Exponential growth
        x = t
        seconds = 0
        while x < z:
            x = k * x + b
            seconds += 1
        print(seconds)

if __name__ == "__main__":
    main()
