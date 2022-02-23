from hw_3.src.mixins import MixinsMatrix
import numpy as np
from os import makedirs
from os.path import join

makedirs(join('artifacts', 'medium'), exist_ok=True)
np.random.seed(0)
a1 = np.random.randint(0, 10, (10, 10))
a2 = np.random.randint(0, 10, (10, 10))

m1 = MixinsMatrix(a1)
m2 = MixinsMatrix(a2)
print(((m1 + m2).values - (a1 + a2)).sum())
print(((m1 * m2).values - (a1 * a2)).sum())
print(((m1 @ m2).values - (a1 @ a2)).sum())

(m1 + m2).to_file(join('artifacts', 'medium', 'matrix+.txt'))
(m1 * m2).to_file(join('artifacts', 'medium', 'matrix*.txt'))
(m1 @ m2).to_file(join('artifacts', 'medium', 'matrix@.txt'))
