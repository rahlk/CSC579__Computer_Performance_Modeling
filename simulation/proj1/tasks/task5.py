from __future__ import division
from __future__ import print_function
import os
import sys
import functools
import pandas as pd

# Update path
root = os.path.join(os.getcwd().split('proj1')[0], 'proj1')
if root not in sys.path:
    sys.path.append(root)

import numpy as np
import multiprocessing
from pdb import set_trace
from Simulator import simulate
from Utils.PlotsUtils import line
from Utils.RandomUtil import Random
from Utils.MisclUtils import TimeUtil

rand = Random()
timer = TimeUtil()

def customer_loss_rate(customers):
    served = np.sum([customer.serviced for customer in customers])
    total = len(customers)
    return served / total

def plot_runtime(x=None, y=None):
    line(x, y, x_label=r"$\rho", y_label=r"Run Times", the_title=r"$\mathrm{Run\ Times\ in\ }\mu\mathrm{s\ vs.\ }\rho$")

def task_5():
    rho_list = np.arange(0.05, 1, 0.1)
    elapsed = []
    print("Rho, Seconds")
    for rho in rho_list:
        start_time = timer.current_time()
        print("{}".format(rho), end=", ")
        serviced = simulate(l = rho, server_lim = 40, max_serviced=100000, L=1, verbose=False)
        end_time = timer.current_time()
        print("{}".format(round(end_time-start_time,2)))
        elapsed.append(end_time-start_time)

def csv_to_plot():
    data = pd.read_csv(os.path.abspath("tasks/task5.csv"))
    plot_runtime(data["Rho"], data["Seconds"])
    set_trace()


if __name__ == "__main__":
    csv_to_plot()
