import collections


def solve():
    try:
        n = int(input())
    except EOFError:
        return
    except ValueError:
        return

    undoubtedly_lucky_numbers = set()

    for x in range(10):
        for y in range(x, 10):
            if x == 0 and y == 0:
                continue

            queue = collections.deque()

            if x > 0:
                queue.append(x)

            if y > 0 and x != y:
                queue.append(y)

            while queue:
                current_num = queue.popleft()

                if current_num > n:
                    continue

                undoubtedly_lucky_numbers.add(current_num)

                if current_num * 10 <= n:
                    next_num_x = current_num * 10 + x
                    if next_num_x <= n:
                        queue.append(next_num_x)

                if x != y:
                    if current_num * 10 <= n:
                        next_num_y = current_num * 10 + y
                        if next_num_y <= n:
                            queue.append(next_num_y)

    print(len(undoubtedly_lucky_numbers))


solve()