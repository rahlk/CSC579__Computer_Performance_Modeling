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
from Utils.PlotsUtils import histogram, line
from pdb import set_trace
from Simulator import simulate

rand = Random()

def customer_loss_rate(customers):
    served = np.sum([customer.serviced for customer in customers])
    total = len(customers)
    return served / total


def plot_loss_rate(x, y):
    if x is None:
        x = np.arange(0.05, 1, 0.1)
    if y is None:
        y = [rand.exponential(lam=0.5) for _ in xrange(10)]
    line(x, y)
    set_trace()


def simulate_partial_func(K, C):
    return simulate(l=0.85, server_lim=K, max_serviced=C, L=1, verbose=False)


def task_2_serial():
    k = np.arange(10, 101, 10)
    C = (1e3, 1e4)
    serviced = [map(functools.partial(
    simulate_partial_func, C=max_serve), k) for max_serve in C]
    set_trace()

def task_2_parallel():
    k = np.arange(10, 101, 10)
    C = (1e3, 1e4)
    pool_0 = multiprocessing.Pool(processes=10)
    serviced_pool = [pool_0.map(functools.partial(
    simulate_partial_func, C=max_serve), k) for max_serve in C]
    set_trace()

if __name__ == "__main__":
    task_2_parallel()
    # plot_loss_rate(x=None, y=None)
