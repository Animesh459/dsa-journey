def main():
    recipe = input().strip()

    nb, ns, nc = map(int, input().split())
    pb, ps, pc = map(int, input().split())
    r = int(input())

    # Count ingredients needed per hamburger
    needB = recipe.count('B')
    needS = recipe.count('S')
    needC = recipe.count('C')

    left, right = 0, 10**13
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        cost = 0
        cost += max(0, needB * mid - nb) * pb
        cost += max(0, needS * mid - ns) * ps
        cost += max(0, needC * mid - nc) * pc

        if cost <= r:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)


if __name__ == "__main__":
    main()
