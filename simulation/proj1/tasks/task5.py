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
from pdb import set_trace
from Simulator import simulate
from Utils.PlotsUtils import line, line2
from Utils.RandomUtil import Random
from Utils.MisclUtils import TimeUtil

rand = Random()
timer = TimeUtil()

# Set seed
rand.set_seed(seed_val=12458)

def customer_loss_rate(customers):
    served = np.sum([customer.serviced for customer in customers])
    total = len(customers)
    return served / total

def plot_runtime(x=None, y=None):
    line(x, y, x_label=r"$\rho$", y_label=r"Run Times", the_title=r"$\mathrm{Run\ Times\ in\ }\mu\mathrm{s\ vs.\ }\rho$")


def plot_runtime_vs_avg(x, y, y_1):
    line2(x, y, x, y_1, label_1="Actual Runtimes", label_2="Expected value of $\rho$", x_label=r"$\rho$", y_label=r"Run Times", the_title=r"$\mathrm{Run\ Times\ in\ }\mu\mathrm{s\ vs.\ }\rho$")


def task_5():
    rho_list = np.arange(0.05, 1, 0.1)
    C = 1e5
    elapsed = []
    for rho in rho_list:
        start_time = timer.current_time()
        serviced = simulate(l = rho, server_lim = 40, max_serviced=C, L=1, verbose=False)
        end_time = timer.current_time()
        elapsed.append(end_time-start_time)

    data = pd.DataFrame([[a,b] for a, b in zip(rho_list, elapsed)], columns=["Rho", "Seconds"])
    data.to_csv(os.path.abspath(os.path.join(root,"tasks/task5.csv")))

def task5_plot():
    data = pd.read_csv(os.path.abspath("tasks/task5.csv"))
    plot_runtime(data["Rho"], data["Seconds"])
    set_trace()


def compare_plot():
    rho_list = np.arange(0.05, 1, 0.1)
    average_rho = [np.mean([rand.exponential(lam=p) for _ in xrange(10000)]) for p in rho_list]
    data = pd.read_csv(os.path.abspath("tasks/task5.csv"))
    plot_runtime(data["Rho"], average_rho)


if __name__ == "__main__":
    task_5()
    task5_plot()
    compare_plot()
