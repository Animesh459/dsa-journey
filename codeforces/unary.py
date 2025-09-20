def solve():
    """
    Calculates the size of the equivalent Unary program for a given Brainfuck program.
    """
    p = input()
    mod = 1000003

    # Mapping from Brainfuck commands to 4-bit binary strings
    mapping = {
        '>': '1000',
        '<': '1001',
        '+': '1010',
        '-': '1011',
        '.': '1100',
        ',': '1101',
        '[': '1110',
        ']': '1111'
    }

    # Concatenate the binary codes
    binary_string = ""
    for char in p:
        binary_string += mapping[char]

    # Convert the binary string to a decimal number modulo 1000003
    decimal_value = 0
    for bit in binary_string:
        decimal_value = (decimal_value * 2 + int(bit)) % mod

    print(decimal_value)

solve()