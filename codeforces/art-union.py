import sys


def solve():
    """
    Reads the input and calculates the completion times for each picture
    in a flow shop scheduling scenario.
    """
    try:
        # Read m and n from the first line
        m, n = map(int, sys.stdin.readline().split())

        # Initialize an array to store the completion time of the last task
        # for each painter. This represents when the painter becomes available again.
        painter_finish_time = [0] * n

        # Process each picture one by one
        for i in range(m):
            # Read the painting times for the current picture
            painting_times = list(map(int, sys.stdin.readline().split()))

            # This variable will store the time the current picture is ready for the next painter.
            # Initially, it's 0 for the first painter.
            picture_ready_time = 0

            # Process the current picture through each painter sequentially
            for j in range(n):
                # The painter can only start when they are available AND the picture is ready.
                # The picture is ready when the previous painter finished their work on it.
                start_time = max(painter_finish_time[j], picture_ready_time)

                # The completion time for this painter on this picture is the start time
                # plus the time it takes them to paint.
                completion_time = start_time + painting_times[j]

                # Update the time this painter becomes free
                painter_finish_time[j] = completion_time

                # The picture is now ready for the next painter at this completion time
                picture_ready_time = completion_time

            # The final completion time for the current picture is the time the last painter
            # finishes their work on it.
            # We don't need to store this in an array, we can print it directly.
            print(picture_ready_time, end=' ')
    except (IOError, ValueError):
        # Handle potential errors during input reading
        return


if __name__ == "__main__":
    solve()