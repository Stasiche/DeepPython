from src.stopwatch import stopwatch
from src.integrate import integrate_process_version, integrate_thread_version

import math
import logging
import os
from collections import defaultdict

n_iter = int(1e4)
cpu_num = os.cpu_count()
results = defaultdict(list)

for name, integrate_fun in zip(('process', 'thread'), (integrate_process_version, integrate_thread_version)):
    os.makedirs(os.path.join('.', 'artifacts', 'medium'), exist_ok=True)
    logging.basicConfig(filename=os.path.join('.', 'artifacts', 'medium', f'log.txt'),
                        level=logging.INFO,
                        format="%(asctime)s;%(levelname)s;%(message)s")
    logger = logging.getLogger(os.path.basename(__file__))

    for n_jobs in range(1, 2 * cpu_num + 1):
        with stopwatch() as t:
            integrate_fun(math.cos, 0, math.pi / 2, n_jobs=n_jobs, n_iter=n_iter, logger=logger)
            results[name].append(t())

with open(os.path.join('.', 'artifacts', 'medium', 'exec_time.txt'), 'w') as f:
    f.write('n_jobs\tprocess\tthread\n')
    for n_jobs, process_time, thread_time in zip(range(1, 2 * cpu_num + 1), results['process'], results['thread']):
        f.write(f'{n_jobs}\t{process_time}\t{thread_time}\n')
