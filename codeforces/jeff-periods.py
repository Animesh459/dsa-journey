def solve():
    n = int(input())
    if n == 0:
        print(0)
        return
    a = list(map(int, input().split()))

    # A dictionary to store the indices for each unique number
    positions = {}
    for i in range(n):
        num = a[i]
        if num in positions:
            positions[num].append(i)
        else:
            positions[num] = [i]

    results = []
    for num, indices in positions.items():
        if len(indices) == 1:
            # A single occurrence forms an AP with a common difference of 0
            results.append((num, 0))
        elif len(indices) > 1:
            # Check for arithmetic progression
            diff = indices[1] - indices[0]
            is_ap = True
            for i in range(2, len(indices)):
                if indices[i] - indices[i-1] != diff:
                    is_ap = False
                    break
            if is_ap:
                results.append((num, diff))

    # Sort results by the number
    results.sort()

    # Print the output
    print(len(results))
    for num, diff in results:
        print(num, diff)

if __name__ == "__main__":
    solve()