def solve():
    n, m = map(int, input().split())
    tasks = list(map(int, input().split()))
    total_time = 0
    current_house = 1
    for task_house in tasks:
        if task_house >= current_house:
            time_to_add = task_house - current_house
        else:
            time_to_add = (n - current_house) + task_house
        total_time += time_to_add
        current_house = task_house
    print(total_time)

solve()