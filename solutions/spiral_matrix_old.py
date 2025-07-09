from itertools import batched
from pprint import pprint
from typing import List


class SpiralMatrix:
    """
    Represents a utility for creating and manipulating a spiral matrix.

    The SpiralMatrix class is designed to create a two-dimensional matrix of size `n x n`,
    and fill it with integers in a spiral pattern. It supports matrix construction and
    spatially ordered value population based on user-defined specifications.
    """

    def __init__(self, n):
        self.n = n
        self.size = n * n
        self.matrix = None
        self.left, self.right = 0, n - 1
        self.top, self.bottom = 0, n - 1
        self.counter = 1

    def create_matrix(self) -> List[List[int]]:
        """
        Constructs a matrix by batching a range of numbers. The range spans from 0 to the `size` attribute
        of the instance. The numbers are grouped into sublists of size `n`, effectively forming a 2D matrix.

        """
        return list(list(batch) for batch in batched(range(self.size), self.n))

    def next_step(self, method, right: bool, bottom: bool):
        """
        Executes the given method with specified parameters and determines the next step in
        the sequence based on an internal counter and size.

        :param method: A callable object representing the method to be executed.
        :param right: A boolean flag specifying a condition passed to the method.
        :param bottom: A boolean flag representing an additional condition passed to the method.
        :return: Returns the result of the method execution if the internal counter is less
                 than the size, otherwise returns None.
        """
        if self.counter > self.size:
            return None
        return method(right, bottom)

    def fill_row(self, right=True, bottom=True):
        """
        Fills a single row in the matrix, incrementing the counter for each position filled.

        This method updates the given row of the matrix based on the current state of
        the attributes. It determines the direction of filling (left-to-right or
        right-to-left) based on the `right` parameter, and whether it operates on the
        top-most or bottom-most available row based on the `bottom` parameter. After
        filling, it adjusts the row index attribute accordingly and invokes the
        next logical step to proceed with filling columns.

        :param right: A boolean value specifying the filling direction.
            If True, fills from left to right; otherwise, fills from right to left.
        :type right: bool
        :param bottom: A boolean value specifying the row to fill.
            If True, fills the bottom-most available row; otherwise, fills the top-most available row.
        :type bottom: bool
        :return: The function or method which determines the next step in the matrix filling process.
        :rtype: Callable
        """
        direction = range(self.left, self.right + 1)
        if not right:
            direction = reversed(direction)
        direction = list(direction)
        row_attr = "top" if bottom else "bottom"
        row = getattr(self, row_attr)

        for i in direction:
            self.matrix[row][i] = self.counter
            self.counter += 1

        setattr(self, row_attr, (row + 1) if bottom else (row - 1))

        return self.next_step(self.fill_col, not right, bottom)

    def fill_col(self, right=True, bottom=True):
        """
        Fills a column of the matrix with sequential values starting from the current
        counter, either from top to bottom or from bottom to top, depending on the
        provided direction. Adjusts left or right column index for the next operation
        after filling the column.

        :param right: Indicates whether to fill the right column (True) or left column
                      (False). Defaults to True.
        :type right: bool
        :param bottom: Indicates the direction of filling. If True, fills from top to
                       bottom; if False, fills from bottom to top. Defaults to True.
        :type bottom: bool
        :return: Result of the next operation to be executed after filling the column.
        :rtype: Any
        """
        direction = range(self.top, self.bottom + 1)
        if not bottom:
            direction = reversed(direction)
        direction = list(direction)
        col_attr = "left" if right else "right"
        col = getattr(self, col_attr)

        for i in direction:
            self.matrix[i][col] = self.counter
            self.counter += 1

        setattr(self, col_attr, (col + 1) if right else (col - 1))

        return self.next_step(self.fill_row, right, not bottom)

    def make_spiral(self):
        """
        Creates a spiral matrix by filling rows with appropriate values.

        Generates a two-dimensional matrix and populates it in a spiral
        pattern by filling the rows in the correct order.

        :return: A two-dimensional list representing the spiral matrix.
        :rtype: list
        """
        self.matrix = self.create_matrix()
        self.fill_row()

        return self.matrix


examples = [
    3,
    4,
    5,
    6,
]


if __name__ == "__main__":
    for example in examples:
        print(f"{example}: \n")
        pprint(SpiralMatrix(example).make_spiral())
