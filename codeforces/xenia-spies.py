def solve():
    import sys
    # Read the first line: n, m, s, f
    # The map(int, sys.stdin.readline().split()) is a common way to read space-separated integers
    try:
        data = sys.stdin.readline().split()
        if not data:
            return
        n, m, s, f = map(int, data)
    except Exception:
        # Handle cases where input might be empty or malformed
        return

    # Read the m watching intervals: (ti, li, ri)
    watch_data = []
    for _ in range(m):
        try:
            line = sys.stdin.readline().split()
            if not line:
                break
            watch_data.append(tuple(map(int, line)))
        except Exception:
            break

    # Determine the desired direction of movement
    # Move towards f. If s < f, move 'R' (Right). If s > f, move 'L' (Left).
    direction = 'R' if s < f else 'L'
    move_val = 1 if s < f else -1

    current_pos = s
    current_time = 1
    watch_idx = 0
    result = []

    # Loop until the note reaches the destination f
    while current_pos != f:
        # --- 1. Check if the current time is a watched step ---
        is_watched_time = False
        l, r = -1, -1  # Default watched range is empty (not watched)

        if watch_idx < m:
            t_watch, l_watch, r_watch = watch_data[watch_idx]
            if current_time == t_watch:
                is_watched_time = True
                l, r = l_watch, r_watch

        # --- 2. Determine the next action ---

        # Desired next position if we make the move
        desired_next_pos = current_pos + move_val

        # Check if the desired move is safe
        action = ''

        if is_watched_time:
            # Check if the current spy and the target spy are watched

            # The giving spy is watched if current_pos is in [l, r]
            giver_watched = (l <= current_pos <= r)

            # The receiving spy is watched if desired_next_pos is in [l, r]
            receiver_watched = (l <= desired_next_pos <= r)

            # A pass is safe if NEITHER the giver NOR the receiver are watched
            is_safe_move = not giver_watched and not receiver_watched

            if is_safe_move:
                # Safe to move towards f
                action = direction
                current_pos = desired_next_pos
            else:
                # Must wait
                action = 'X'
        else:
            # Not a watched time, any move is safe
            action = direction
            current_pos = desired_next_pos

        # Record the action
        result.append(action)

        # --- 3. Advance time and watch index ---
        current_time += 1
        if is_watched_time:
            # Move to the next watched interval
            watch_idx += 1

    # Print the final sequence of actions
    print("".join(result))


solve()