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
# Set seed
rand.set_seed(seed_val=12458)


def customer_loss_rate(server):
    denied = len(server.rejected)
    total = len(server.rejected + server.processed)
    return denied / total


def plot_loss_rate(x, y_1, y_2):
    line2(x, y_1, x, y_2, label_1="C=$10^3$", label_2="C=$10^5$",
          x_label=r"$\rho$", y_label=r"CLR",
          the_title=r"$\mathrm{CLR\ vs.\ }\rho$")
    set_trace()


def task_1_serial():
    rho_list = np.arange(0.05, 1, 0.1)
    C = [1e3, 1e5]
    serviced_pool = [map(
        functools.partial(simulate, server_lim=20, max_serviced=lim, L=1,
                          verbose=True), rho_list) for lim in C]
    set_trace()


def task_1_parallel():
    C = [1e3, 1e4]
    rho_list = np.arange(0.05, 1, 0.1)
    pool_0 = multiprocessing.Pool(processes=10)
    CLR = []
    for lim in C:
        serviced_pool = pool_0.map(
            functools.partial(simulate, server_lim=20, max_serviced=lim, L=1,
                              verbose=False), rho_list)
        CLR.append([customer_loss_rate(s) for s in serviced_pool])

    plot_loss_rate(rho_list, CLR[0], CLR[1])
    # set_trace()


if __name__ == "__main__":
    task_1_parallel()
    # plot_loss_rate(x=None, y=None)
