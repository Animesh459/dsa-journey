import sys

sys.setrecursionlimit(2000)


def solve():
    s = sys.stdin.readline().strip()
    if not s:
        return

    try:
        m = int(sys.stdin.readline().strip())
    except:
        return

    available_weights = [i + 1 for i, char in enumerate(s) if char == '1']

    result = []

    memo = set()

    def dfs(step, last_w, diff):
        if step == m:
            return True

        state = (step, last_w, diff)
        if state in memo:
            return False

        for w in available_weights:
            if w != last_w and w > diff:
                result.append(w)
                if dfs(step + 1, w, w - diff):
                    return True
                result.pop()  # Backtrack

        memo.add(state)
        return False

    if dfs(0, 0, 0):
        print("YES")
        print(*(result))
    else:
        print("NO")


if __name__ == "__main__":
    solve()