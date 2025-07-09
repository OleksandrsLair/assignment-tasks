from pprint import pprint


def spiral_matrix(n: int):
    """
    Generates a spiral matrix of size n x n, starting from 1 in the top-left
    corner and spiraling clockwise. The function dynamically constructs the
    matrix by iteratively updating its edges and filling in numbers in a
    spiral pattern. The result is an n x n 2D list.

    :param n: Size of the matrix to generate, representing both the number
        of rows and columns. Must be a positive integer.
    :type n: int

    :return: A 2D list representing the spiral matrix of dimensions n x n,
        where n is the input size. The matrix is filled with sequential
        numbers starting from 1, organized in a clockwise spiral pattern.
    :rtype: list[list[int]]
    """
    # top
    matrix = [list(range(1, n + 1))]

    # right side
    if n >= 3:
        matrix.extend([[i] for i in range(n + 1, 2 * n - 1)])

    # bottom
    if n >= 2:
        matrix.append(list(reversed(range(2 * n - 1, 3 * n - 1))))

    top, bottom, left, right = 1, n - 1, 0, n - 1
    counter = 3 * n - 1
    while top < bottom or left < right:
        # left side
        for i in reversed(range(top, bottom)):
            matrix[i].insert(left, counter)
            counter += 1
        left += 1

        # top side
        for i in range(left, right):
            matrix[top].insert(i, counter)
            counter += 1
        top += 1

        # right side
        for i in range(top, bottom):
            matrix[i].insert(-(n - right), counter)
            counter += 1
        right -= 1

        # bottom side
        for i in range(left, right):
            matrix[bottom - 1].insert(-i - 1, counter)
            counter += 1
        bottom -= 1

    return matrix


examples = [
    3,
    4,
    5,
    6,
    7,
]


if __name__ == "__main__":
    for size in examples:
        print(f"{size}: \n")
        pprint(spiral_matrix(size), indent=2)
