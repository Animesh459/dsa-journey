import math

HPY, ATKY, DEFY = map(int, input().split())
HPM, ATKM, DEFM = map(int, input().split())
h, a, d = map(int, input().split())

INF = 10**18
answer = INF

# Try all reasonable increases of ATK and DEF
for add_atk in range(0, 201):
    for add_def in range(0, 201):
        # Yang's effective damage to monster per second
        damage_to_monster = ATKY + add_atk - DEFM
        if damage_to_monster <= 0:
            continue  # cannot hurt the monster at all

        # Seconds needed to kill the monster
        time_to_kill = math.ceil(HPM / damage_to_monster)

        # Monster's damage to Yang per second
        damage_to_yang = max(0, ATKM - (DEFY + add_def))

        # Total damage Yang will take
        total_damage = damage_to_yang * time_to_kill

        # HP needed to survive (must stay > 0)
        required_hp = max(0, total_damage + 1 - HPY)

        # Total cost
        cost = (
            add_atk * a +
            add_def * d +
            required_hp * h
        )

        answer = min(answer, cost)

print(answer)
