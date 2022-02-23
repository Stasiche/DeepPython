from hw_3.src.hard_matrix import HardMatrix
import numpy as np
from os import makedirs
from os.path import join

makedirs(join('artifacts', 'hard'), exist_ok=True)
a = np.array([[0, 2],
              [1, 2]])
b = np.array([[1, 0],
              [0, 1]])

c = np.array([[7, 2],
              [1, 2]])
d = b

A = HardMatrix(a)
B = HardMatrix(b)
C = HardMatrix(c)
D = HardMatrix(d)

print((hash(A) == hash(C)) and (A != C) and (B == D) and ((A @ B) != (C @ D)))

for name, mat in zip(('A', 'B', 'C', 'D', 'AB', 'CD'), (A, B, C, D, A@B, C@D)):
    with open(join('artifacts', 'hard', f'{name}.txt'), 'w') as f:
        f.writelines(map(lambda x: str(x) + '\n', mat.values.tolist()))

with open(join('artifacts', 'hard', f'hash.txt'), 'w') as f:
    f.write(str((A@B).__hash__()))
    f.write('\n')
    f.write(str((C@D).__hash__()))

