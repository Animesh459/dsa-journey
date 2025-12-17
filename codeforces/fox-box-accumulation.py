import heapq

def minimal_piles(n, strengths):
    strengths.sort()
    piles = []  # min-heap of pile heights

    for x in strengths:
        if piles and piles[0] <= x:
            smallest = heapq.heappop(piles)
            heapq.heappush(piles, smallest + 1)
        else:
            heapq.heappush(piles, 1)

    return len(piles)

n = int(input().strip())
strengths = list(map(int, input().split()))
print(minimal_piles(n, strengths))
