import math


def solve():
    areas = list(map(int, input().split()))
    a1, a2, a3 = areas[0], areas[1], areas[2]

    # Let the edge lengths be x, y, z.
    # The areas of the three faces with a common vertex are:
    # x * y = a1
    # x * z = a2
    # y * z = a3

    # We can multiply these three equations together:
    # (x * y) * (x * z) * (y * z) = a1 * a2 * a3
    # x^2 * y^2 * z^2 = a1 * a2 * a3
    # (x * y * z)^2 = a1 * a2 * a3

    # Taking the square root of both sides:
    # x * y * z = sqrt(a1 * a2 * a3)

    # Let's call this product P: P = x * y * z
    # Then we can find x, y, and z:
    # x = (x * y * z) / (y * z) = P / a3
    # y = (x * y * z) / (x * z) = P / a2
    # z = (x * y * z) / (x * y) = P / a1

    # First, calculate the product of the areas.
    product_of_areas = a1 * a2 * a3

    # Then, find the product of the edge lengths.
    product_of_edges = int(math.sqrt(product_of_areas))

    # Now, find the individual edge lengths.
    x = product_of_edges // a3
    y = product_of_edges // a2
    z = product_of_edges // a1

    # A parallelepiped has 12 edges:
    # 4 edges of length x
    # 4 edges of length y
    # 4 edges of length z

    # The sum of all edge lengths is 4x + 4y + 4z = 4 * (x + y + z)
    sum_of_edges = 4 * (x + y + z)

    print(sum_of_edges)


solve()