import sys


def solve():
    n, m = map(int, sys.stdin.readline().split())

    # Use a set to store prohibited pairs for O(1) average lookup
    prohibited = set()
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        # Store pairs in a canonical order (e.g., sorted) to handle (a,b) and (b,a)
        prohibited.add(tuple(sorted((u, v))))

    # Find a city that is NOT part of ANY prohibited pair.
    # The problem guarantees a solution exists, so such a city must exist.
    central_city = -1
    all_cities = set(range(1, n + 1))
    prohibited_cities = set()
    for u, v in prohibited:
        prohibited_cities.add(u)
        prohibited_cities.add(v)

    # Find a city that is not in the set of prohibited cities
    unrestricted_cities = list(all_cities - prohibited_cities)

    if unrestricted_cities:
        central_city = unrestricted_cities[0]
    else:
        # This case should not be reached based on the problem guarantee,
        # but as a fallback, we could choose any city and fill in the missing connections
        # in a more complex way. However, given the problem constraints, this is unnecessary.
        pass

    print(n - 1)

    for i in range(1, n + 1):
        if i != central_city:
            print(central_city, i)


# Call the function
solve()