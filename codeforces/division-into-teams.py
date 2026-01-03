import sys


def main():
    input = sys.stdin.readline

    n = int(input())
    skills = list(map(int, input().split()))

    # Pair skills with original indices (1-based)
    players = [(skills[i], i + 1) for i in range(n)]

    # Sort by skill descending
    players.sort(reverse=True)

    team1 = []
    team2 = []

    # Alternate assignment
    for i, (_, idx) in enumerate(players):
        if i % 2 == 0:
            team1.append(idx)
        else:
            team2.append(idx)

    # Output
    print(len(team1))
    print(*team1)
    print(len(team2))
    print(*team2)


if __name__ == "__main__":
    main()
