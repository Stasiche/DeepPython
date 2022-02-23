from hw_3.src.matrix import Matrix
import numpy as np
from os import makedirs
from os.path import join

makedirs(join('artifacts', 'easy'), exist_ok=True)
np.random.seed(0)
a1 = np.random.randint(0, 10, (10, 10))
a2 = np.random.randint(0, 10, (10, 10))

m1 = Matrix(a1)
m2 = Matrix(a2)
print(((m1 + m2).values - (a1 + a2)).sum())
print(((m1 * m2).values - (a1 * a2)).sum())
print(((m1 @ m2).values - (a1 @ a2)).sum())

with open(join('artifacts', 'easy', 'matrix+.txt'), 'w') as f:
    f.writelines(map(lambda x: str(x) + '\n', (m1 + m2).values.tolist()))

with open(join('artifacts', 'easy', 'matrix*.txt'), 'w') as f:
    f.writelines(map(lambda x: str(x) + '\n', (m1 * m2).values.tolist()))

with open(join('artifacts', 'easy', 'matrix@.txt'), 'w') as f:
    f.writelines(map(lambda x: str(x) + '\n', (m1 @ m2).values.tolist()))