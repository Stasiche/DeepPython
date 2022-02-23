import numpy as np


class Matrix:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        if not ((self.values.shape[0] == other.values.shape[0]) and (self.values.shape[1] == other.values.shape[1])):
            raise ValueError('Incorrect dims')

        res = np.empty_like(self.values)
        for i, (row_1, row_2) in enumerate(zip(self.values, other.values)):
            for j, (el_1, el_2) in enumerate(zip(row_1, row_2)):
                res[i][j] = el_1 + el_2
        return Matrix(res)

    def __mul__(self, other):
        if not ((self.values.shape[0] == other.values.shape[0]) and (self.values.shape[1] == other.values.shape[1])):
            raise ValueError('Incorrect dims')

        res = np.empty_like(self.values)
        for i, (row_1, row_2) in enumerate(zip(self.values, other.values)):
            for j, (el_1, el_2) in enumerate(zip(row_1, row_2)):
                res[i][j] = el_1 * el_2
        return Matrix(res)

    def __matmul__(self, other):
        if not (self.values.shape[1] == other.values.shape[0]):
            raise ValueError('Incorrect dims')

        res = np.zeros((self.values.shape[0], other.values.shape[1]), dtype=int)
        for i in range(self.values.shape[0]):
            for j in range(other.values.shape[1]):
                for k in range(self.values.shape[1]):
                    res[i, j] += self.values[i, k] * other.values[k, j]
        return Matrix(res)

