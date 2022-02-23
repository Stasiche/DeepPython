import numpy as np
import numbers


class FileWriterMixin:
    def to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))


class StrReprMixin:
    def __init__(self, values):
        self.values = values

    def __str__(self):
        return '|\t' + '\n|\t'.join(['\t|\t'.join(map(str, row)) + '\t|' for row in self.values])

    def __repr__(self):
        return f'type: {type(self)} values: {self.values}'


class GetSetMixin:
    def __init__(self, values):
        self.values = values

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, value):
        self.__values = value


class ArithmeticMixin(np.lib.mixins.NDArrayOperatorsMixin):
    def __init__(self, values):
        self.values = values

    _HANDLED_TYPES = (np.ndarray, numbers.Number)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        for x in inputs:
            if not isinstance(x, self._HANDLED_TYPES + (ArithmeticMixin,)):
                return NotImplemented
        inputs = (x.values for x in inputs)

        return type(self)(getattr(ufunc, method)(*inputs, **kwargs))


class MixinsMatrix(GetSetMixin, FileWriterMixin, StrReprMixin, ArithmeticMixin):
    pass
