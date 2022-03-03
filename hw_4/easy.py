from src.fib import fib
from src.stopwatch import stopwatch
from threading import Thread
from multiprocessing import Process
from os import makedirs
from os.path import join

n = int(1e5)

with stopwatch() as t:
    for _ in range(10):
        fib(n)
sync_time = t()

with stopwatch() as t:
    jobs = []
    for _ in range(10):
        jobs.append(Thread(target=fib, args=(n,)))
        jobs[-1].start()

    for job in jobs:
        job.join()
thread_time = t()

with stopwatch() as t:
    jobs = []
    for _ in range(10):
        jobs.append(Process(target=fib, args=(n,)))
        jobs[-1].start()

    for job in jobs:
        job.join()
process_time = t()

makedirs(join('.', 'artifacts'), exist_ok=True)
with open(join('.', 'artifacts', 'easy.txt'), 'w') as f:
    f.write(f'Sync time: {sync_time}\n'
            f'Thread time: {thread_time}\n'
            f'Process time: {process_time}')

