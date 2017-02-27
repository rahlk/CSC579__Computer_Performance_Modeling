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


def average_wait_time(server):
    return np.mean([customer.get_wait_time() for customer in server.processed])


def plot_mean_wait_time(x, wait_time):
    line(x, wait_time, x_label=r"$\rho$", y_label=r"Wait Times", the_title=r"$\mathrm{Wait\ Times\ in\ milliseconds\ vs.\ }\rho$")
    set_trace()


def task_4():
    rho_list = np.arange(0.05, 1, 0.1)
    C = 1e2
    wait_time = []
    for rho in rho_list:
        serviced_pool = simulate(l = rho, server_lim = 100, max_serviced=lim, L=1, verbose=False)
        wait_time.append(average_wait_time(serviced_pool)])
    plot_mean_wait_time(rho_list, wait_time)


if __name__ == "__main__":
    plot_loss_rate()
