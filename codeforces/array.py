def solve():

    n = int(input())


    arr = list(map(int, input().split()))


    negatives = []
    positives = []
    zeros = []

    for x in arr:
        if x < 0:
            negatives.append(x)
        elif x > 0:
            positives.append(x)
        else:
            zeros.append(x)

    set1 = [negatives.pop(0)]

    if len(positives) > 0:
        set2 = positives

    else:

        set2 = [negatives.pop(0), negatives.pop(0)]


    set3 = zeros + negatives + positives


    print(len(set1), *set1)

    # Print Set 2
    print(len(set2), *set2)

    # Print Set 3
    print(len(set3), *set3)

solve()