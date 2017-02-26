from __future__ import division
from __future__ import print_function
import os
import sys
import functools

# Update path
root = os.path.join(os.getcwd().split('proj1')[0], 'proj1')
if root not in sys.path:
    sys.path.append(root)

import numpy as np
import multiprocessing as mp
from Simulator import simulate


def customer_loss_rate(customers):
    served = np.sum([customer.serviced for customer in customers])
    total = len(customers)
    return served / total


def task_1_serial():
    k = np.arange(0.05, 1, 0.1)
    C = (1e3, 1e5)
    customers = simulate(l=k, )
    pass


def task_1_parallel():
    k = np.arange(0.05, 1, 0.1)
    C = (1e3, 1e5)
    pool_0 = mp.Pool
    pool_0.map(functools.partial(l, K = 20, C=C[0], L=1), k)
    # pool_1 = mp.Pool(functools.partial(l, K = 20, C=C[1], L=1), k)
    pass
