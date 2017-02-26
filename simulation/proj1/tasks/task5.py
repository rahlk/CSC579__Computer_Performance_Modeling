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
import multiprocessing
from Utils.RandomUtil import Random
from Utils.PlotsUtils import line2
from pdb import set_trace
from Simulator import simulate

rand = Random()


def customer_loss_rate(customers):
    served = np.sum([customer.serviced for customer in customers])
    total = len(customers)
    return served / total

def plot_loss_rate(x=None, CLR=None, CLR_theoritical=None):
    if x is None:
        x = np.arange(0.05, 1, 0.1)
    if y is None:
        y = [rand.exponential(lam=0.5) for _ in xrange(10)]
    line(x, y)
    set_trace()

def task_5_serial():
    rho_list = np.arange(0.05, 1, 0.1)
    C = (1e3, 1e5)
    serviced_pool = [map(functools.partial(simulate, server_lim = 20, max_serviced=lim, L=1, verbose=False), rho_list) for lim in C]
    set_trace()

def task_5_parallel():
    rho_list = np.arange(0.05, 1, 0.1)
    C = (1e3, 1e5)

    pool_0 = multiprocessing.Pool(processes=10)

    serviced_pool = [pool_0.map(functools.partial(simulate, server_lim = 20, max_serviced=lim, L=1, verbose=False), rho_list) for lim in C]

    CLR = [[customer_loss_rate(s) for s in serviced] for serviced in serviced_pool]
    CLR_theoritical = [theoritical_loss_rate(r, K=20) for r in rho_list]

    set_trace()

if __name__ == "__main__":
    # task_5_parallel()
    plot_loss_rate()
