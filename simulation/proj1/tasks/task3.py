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
import pandas as pd
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


def theoritical_loss_rate(rho, K):
    """
                        k
               (1 - p) p
      CLR =    ----------
                     k + 1
                1 - p

    """
    return (1-rho) * rho ** K / (1 - rho ** (K+1))


def plot_loss_rate(x, CLR, CLR_theoritical, label):
    line2(x, CLR, x, CLR_theoritical, label_1=label, label_2="CLR (Theoritical)", x_label=r"$\rho$", y_label=r"CLR", the_title=r"CLR (Sim) vs. CLR (Theoritical)")


def task_3():
    C = (1e1, 1e2)
    rho_list = np.arange(0.05, 1, 0.1)
    pool_0 = multiprocessing.Pool(processes=10)
    CLR_theoritical = [theoritical_loss_rate(r, K=20) for r in rho_list]

    CLR = []
    for lim in C:
        serviced_pool = pool_0.map(
            functools.partial(simulate, server_lim=20, max_serviced=lim, L=1,
                              verbose=False), rho_list)
        CLR.append([customer_loss_rate(s) for s in serviced_pool])

    data = pd.DataFrame([[a,b,c,d] for a, b, c, d in zip(rho_list, CLR[0], CLR[1], CLR_theoritical)], columns=["Rho", "CLR (C=1000)", "CLR (C=100000)", "CLR (Theoritic)"])
    data.to_csv(os.path.abspath(os.path.join(root,"tasks/task3.csv")))


def task3_plot():
    data = pd.read_csv(os.path.abspath(os.path.join(root,"tasks/task3.csv")))
    plot_loss_rate(data["Rho"], data["CLR (C=1000)"], data["CLR (Theoritic)"], label="CLR (C=1000)")
    plot_loss_rate(data["Rho"], data["CLR (C=100000)"], data["CLR (Theoritic)"], label="CLR (C=100000)")

    set_trace()


if __name__ == "__main__":
    task_3()
    # plot_loss_rate()
