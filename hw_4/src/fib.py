from typing import List


def fib(n: int) -> List[int]:
    prev, pprev, res = 1, 0, [0, 1]
    for _ in range(n-2):
        pprev, prev = prev, prev + pprev
        res.append(prev)
    return res