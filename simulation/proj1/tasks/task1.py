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


def plot_loss_rate(x, y_1, y_2, label_1, label_2):
    line2(x, y_1, x, y_2, label_1="C=$10^3$", label_2="C=$10^5$",
          x_label=r"$\rho$", y_label=r"CLR",
          the_title=r"$\mathrm{CLR\ vs.\ }\rho$")
    set_trace()


def task_1():
    C = [1e3, 1e5]
    rho_list = np.arange(0.05, 1, 0.1)
    pool_0 = multiprocessing.Pool(processes=10)
    CLR = []
    for lim in C:
        serviced_pool = pool_0.map(
            functools.partial(simulate, server_lim=20, max_serviced=lim, L=1,
                              verbose=False), rho_list)
        CLR.append([customer_loss_rate(s) for s in serviced_pool])

    data = pd.DataFrame([[a,b,c] for a, b, c in zip(rho_list, CLR[0], CLR[1])], columns=["Rho", "CLR (C=1e3)", "CLR (C=1e5)"])
    data.to_csv(os.path.abspath(os.path.join(root,"tasks/task1.csv")))

def task1_plot():
    data = pd.read_csv(os.path.abspath(os.path.join(root,"tasks/task1.csv")))
    plot_loss_rate(data["Rho"], data["CLR (C=1e3)"], data["CLR (C=1e5)"], label_1="CLR (C=1e3)", label_2="CLR (C=1e5)")


if __name__ == "__main__":
    # task_1()
    task1_plot()
    # plot_loss_rate(x=None, y=None)
