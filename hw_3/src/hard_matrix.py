import numpy as np


class HashMixin:
    def __init__(self, values):
        self.values = values

    def __hash__(self):
        # хэш -- сумма элементов матрицы по модулю 7
        return int(sum(map(sum, self.values)) % 7)


class HardMatrix(HashMixin):
    __hash__ = HashMixin.__hash__

    def __init__(self, values):
        super().__init__(values)
        self.__cache = {}

    def __eq__(self, other):
        return np.array_equal(self.values, other.values)

    def __ne__(self, other):
        return not np.array_equal(self.values, other.values)

    def __add__(self, other):
        if not ((self.values.shape[0] == other.values.shape[0]) and (self.values.shape[1] == other.values.shape[1])):
            raise ValueError('Incorrect dims')

        res = np.empty_like(self.values)
        for i, (row_1, row_2) in enumerate(zip(self.values, other.values)):
            for j, (el_1, el_2) in enumerate(zip(row_1, row_2)):
                res[i][j] = el_1 + el_2
        return HardMatrix(res)

    def __mul__(self, other):
        if not ((self.values.shape[0] == other.values.shape[0]) and (self.values.shape[1] == other.values.shape[1])):
            raise ValueError('Incorrect dims')

        res = np.empty_like(self.values)
        for i, (row_1, row_2) in enumerate(zip(self.values, other.values)):
            for j, (el_1, el_2) in enumerate(zip(row_1, row_2)):
                res[i][j] = el_1 * el_2
        return HardMatrix(res)

    def __matmul__(self, other):
        if not (self.values.shape[1] == other.values.shape[0]):
            raise ValueError('Incorrect dims')

        key = tuple(sorted((self.__hash__(), other.__hash__())))
        if key in self.__cache:
            return self.__cache[key]

        res = np.zeros((self.values.shape[0], other.values.shape[1]), dtype=int)
        for i in range(self.values.shape[0]):
            for j in range(other.values.shape[1]):
                for k in range(self.values.shape[1]):
                    res[i, j] += self.values[i, k] * other.values[k, j]
        res = HardMatrix(res)
        self.__cache[key] = res
        return res
