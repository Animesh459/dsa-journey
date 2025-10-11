import sys


# Set a high recursion limit for safety, though not strictly needed for this iterative solution.
# sys.setrecursionlimit(2000)

def solve():
    """
    Reads the array and calculates the total number of magical subarrays.
    A magical subarray is one where all elements are identical.
    The total number of subarrays in a contiguous run of length k is k * (k + 1) // 2.
    """
    try:
        # Fast input reading
        # Read N (not strictly needed, but included for completeness)
        try:
            n_str = sys.stdin.readline()
            if not n_str:
                return
            n = int(n_str.strip())
        except EOFError:
            return

        # Read the array A
        a = list(map(int, sys.stdin.readline().split()))

    except Exception as e:
        # Handle potential EOF or malformed input gracefully
        # print(f"Error reading input: {e}", file=sys.stderr)
        return

    # Total count of magical subarrays, needs to be a 64-bit integer (Python handles this automatically)
    total_count = 0

    # Use 'i' as the starting index of the current contiguous run
    i = 0
    n = len(a)

    while i < n:
        # 'j' will be the pointer that finds the end of the current run of identical numbers
        j = i + 1

        # Extend 'j' as long as the elements are the same as the start of the run (a[i])
        while j < n and a[j] == a[i]:
            j += 1

        # The length of the current magical run is the difference between the end and start pointers
        run_length = j - i

        # Calculate the number of subarrays (magical) within this run: k * (k + 1) / 2
        # This is the formula for the sum of the first 'k' integers (triangular number).
        # We use integer division // since the result is always an integer.
        subarrays_in_run = run_length * (run_length + 1) // 2

        # Add the count from this run to the total
        total_count += subarrays_in_run

        # Move the start pointer 'i' to the beginning of the next run (where 'j' stopped)
        i = j

    # Print the final result
    print(total_count)


if __name__ == "__main__":
    solve()
