import math
import sys

# ... (PRIME_SET and MAX_SQRT_X definitions remain the same) ...
MAX_SQRT_X = 10 ** 6


def sieve_of_eratosthenes(limit):
    # ... (function body remains the same) ...
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
    primes = set()
    for p in range(2, limit + 1):
        if is_prime[p]:
            primes.add(p)
    return primes


PRIME_SET = sieve_of_eratosthenes(MAX_SQRT_X)


def is_t_prime(x, prime_set):
    # ... (function body remains the same) ...
    if x < 4:
        return False

    # Calculate the integer square root.
    sqrt_x = int(math.sqrt(x))

    # Check if x is a perfect square (Step 1)
    if sqrt_x * sqrt_x != x:
        return False

    # Check if the square root is a prime number (Step 2)
    return sqrt_x in prime_set


def solve():
    """
    Reads the input using standard input() and determines for each number
    if it is a T-prime.
    """
    try:
        # Read n (number of elements) - This line is skipped in the logic
        # but needs to be read from the input stream.
        try:
            # Use input() instead of sys.stdin.readlines() for reliability
            n_str = sys.stdin.readline().strip()
            if not n_str:
                return  # Exit if first line is empty

            # Read the array of numbers on the second line
            # Use sys.stdin.readline() for fast, line-by-line reading
            line_of_numbers = sys.stdin.readline().strip()
            if not line_of_numbers:
                return  # Exit if second line is empty

            # Convert to integers
            x_values = [int(val) for val in line_of_numbers.split()]

        except EOFError:
            return
        except ValueError:
            # Catch errors if conversion to int fails
            return
        except Exception:
            # Catch all other input errors
            return

    except Exception:
        return  # Outer try-except for general issues

    results = []
    for x in x_values:
        if is_t_prime(x, PRIME_SET):
            results.append("YES")
        else:
            results.append("NO")

    # Use sys.stdout.write for fast output
    sys.stdout.write('\n'.join(results) + '\n')


# Execute the solution function
if __name__ == "__main__":
    solve()