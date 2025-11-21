import math
import sys


def solve():
    try:
        line1 = sys.stdin.readline().split()
        if not line1:
            return
        n = int(line1[0])
        vb = int(line1[1])
        vs = int(line1[2])

        x = list(map(int, sys.stdin.readline().split()))

        line3 = sys.stdin.readline().split()
        xu = int(line3[0])
        yu = int(line3[1])

    except:
        return

    min_total_time = float('inf')
    optimal_stop_index = -1
    min_run_distance = float('inf')

    for i in range(1, n):
        xi = x[i]

        bus_time = xi / vb

        run_distance_sq = (xu - xi) ** 2 + yu ** 2
        run_distance = math.sqrt(run_distance_sq)

        run_time = run_distance / vs

        total_time = bus_time + run_time

        current_stop_index = i + 1

        if total_time < min_total_time:
            min_total_time = total_time
            optimal_stop_index = current_stop_index
            min_run_distance = run_distance

        elif math.isclose(total_time, min_total_time, rel_tol=1e-9):
            if run_distance < min_run_distance:
                min_run_distance = run_distance
                optimal_stop_index = current_stop_index

    print(optimal_stop_index)


if __name__ == "__main__":
    solve()