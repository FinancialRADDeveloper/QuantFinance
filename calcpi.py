from random import random
from numba import njit, jit


@jit
def calc_pi_numba(num_attempts: int) -> float:
    inside = 0

    for _ in range(num_attempts):
        x = random()
        y = random()

        if x ** 2 + y ** 2 <= 1:
            inside += 1

    return 4 * inside / num_attempts

@njit
def calc_pi_numba_njit(num_attempts: int) -> float:
    inside = 0

    for _ in range(num_attempts):
        x = random()
        y = random()

        if x ** 2 + y ** 2 <= 1:
            inside += 1

    return 4 * inside / num_attempts

def calc_pi_quick(num_attempts: int) -> float:
    from random import random

    inside = 0

    for _ in range(num_attempts):
        x = random()
        y = random()

        if x ** 2 + y ** 2 <= 1:
            inside += 1

    return 4 * inside / num_attempts


def multi_calc_pi(num_attempts: int, verbose=False) -> float:
    from multiprocessing import Pool
    from random import random
    import os
    from statistics import mean

    # lets leave one spare for OS related things so everything doesn't freeze up
    num_cpus = os.cpu_count() - 1
    # print('Num of CPUS: {}'.format(num_cpus))

    try:
        attempts_to_try_in_process = int(num_attempts / num_cpus)
        pool = Pool(num_cpus)
        # what I am trying to do here is get the calc happening over n-1 Cpus each with an even
        # split of the num_attempts. i.e. 150 attempts over 15 CPU will lead to 10 each then the mean avg
        # of the returned list being returned.
        data_outputs = pool.map(calc_pi_quick, [attempts_to_try_in_process] * num_cpus)
        return mean(data_outputs)
    finally:  # To make sure processes are closed in the end, even if errors happen
        pool.close()
        pool.join()


def multi_calc_pi_numba(num_attempts: int, verbose=False) -> float:
    from multiprocessing import Pool
    from random import random
    import os
    from statistics import mean

    # lets leave one spare for OS related things so everything doesn't freeze up
    num_cpus = os.cpu_count() - 1
    # print('Num of CPUS: {}'.format(num_cpus))

    try:
        attempts_to_try_in_process = int(num_attempts / num_cpus)
        pool = Pool(num_cpus)
        # what I am trying to do here is get the calc happening over n-1 Cpus each with an even
        # split of the num_attempts. i.e. 150 attempts over 15 CPU will lead to 10 each then the mean avg
        # of the returned list being returned.
        data_outputs = pool.map(calc_pi_numba, [attempts_to_try_in_process] * num_cpus)
        return mean(data_outputs)
    finally:  # To make sure processes are closed in the end, even if errors happen
        pool.close()
        pool.join()
