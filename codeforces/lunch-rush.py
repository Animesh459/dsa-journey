# Read n (number of restaurants) and k (time available)
n, k = map(int, input().split())

max_joy = -10 ** 18  # Start with a very small number to handle negative joys

for _ in range(n):
    f, t = map(int, input().split())
    if t > k:
        joy = f - (t - k)  # Late, so reduce joy
    else:
        joy = f  # On time, full joy

    max_joy = max(max_joy, joy)  # Keep track of maximum joy

print(max_joy)
