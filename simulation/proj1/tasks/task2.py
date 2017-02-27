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
# Set seed
rand.set_seed(seed_val=12458)


def customer_loss_rate(server):
    denied = len(server.rejected)
    total = len(server.rejected + server.processed)
    return denied / total


def plot_loss_rate(x, y):
    if x is None:
        x = np.arange(0.05, 1, 0.1)
    if y is None:
        y = [rand.exponential(lam=0.5) for _ in xrange(10)]
    line(x, y)
    set_trace()


def simulate_partial_func(K, C):
    return simulate(l=0.85, server_lim=K, max_serviced=C, L=1, verbose=False)


def task_2():
    queue_size = np.arange(5, 101, 10)
    C = (1e2, 1e3)
    pool_0 = multiprocessing.Pool(processes=10)
    CLR = []
    for max_serve in C:
        serviced_pool = pool_0.map(functools.partial(simulate_partial_func, C=max_serve), queue_size)
        CLR.append([customer_loss_rate(s) for s in serviced_pool])

    data = pd.DataFrame([[a,b,c] for a, b, c in zip(queue_size, CLR[0], CLR[1])], columns=["K", "CLR (C=1e3)", "CLR (C=1e5)"])
    data.to_csv(os.path.abspath(os.path.join(root,"tasks/task2.csv")))


def task2_plot():
    data = pd.read_csv(os.path.abspath(os.path.join(root,"tasks/task2.csv")))
    plot_loss_rate(data["K"], data["CLR (C=1e3)"], data["CLR (C=1e5)"], label_1="CLR (C=1e3)", label_2="CLR (C=1e5)")
    set_trace()


if __name__ == "__main__":
    task_2()
    task2_plot()
