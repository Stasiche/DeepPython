import concurrent.futures


def ds(arg):
    f, x, step, logger = arg
    logger.info(f'Starting task with args: {str(dict(x=round(x, 4), step=round(step, 4)))}')
    return f(x) * step


def integrate_process_version(f, a, b, *, n_jobs=1, n_iter=1000, logger=None):
    step = (b - a) / n_iter
    args = [(f, a + i * step, step, logger) for i in range(n_iter)]
    with concurrent.futures.ProcessPoolExecutor(max_workers=n_jobs) as executor:
        res = list(executor.map(ds, args))

    return sum(res)


def integrate_thread_version(f, a, b, *, n_jobs=1, n_iter=1000, logger=None):
    step = (b - a) / n_iter
    args = [(f, a + i * step, step, logger) for i in range(n_iter)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=n_jobs) as executor:
        res = list(executor.map(ds, args))

    return sum(res)
