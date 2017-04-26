"""
Task 1

Plot average customer waiting time vs. rho (0.05, 0.15, ... , 0.95).
"""

from __future__ import print_function
from __future__ import division
import os, sys

root = os.path.join(os.getcwd().split("proj3")[0], "proj3")
if not root in sys.path:
    sys.path.append(root)

import numpy as np
import pandas as pd
from pdb import set_trace
from Utils.SimUtil2 import Simulation
from Utils.MscUtil import Params
from Utils.StatsUtil import mean_confidence_interval as mci
from scipy import stats

def run_exponential():
    print("Exponential M/M/m")
    for decip in ["FCFS", "SJF"]:
        print(decip)
        sim = Simulation(
            params=Params(distribution="exp", dicipline=decip,
                          C=int(1e5), rho=0.5,
                          lmbd=0.001, mu=1 / 3000))
        sim = sim.run_simulation()
        service_times = [cust.service_time for cust in sim.customers]
        _, edges = np.histogram(service_times, bins=100)
        slowdown = []
        for lo, hi in zip(edges[:-1], edges[1:]):
            slowdown.append(np.mean(np.nan_to_num([cust.wait_time / cust.service_time for cust in
                        sim.customers if lo < cust.service_time <= hi])))
        # set_trace()
        nans = np.where(np.isnan(slowdown))
        slowdown = np.nan_to_num(slowdown)
        for nan_id in nans[0]:
            slowdown[nan_id] = np.mean(slowdown[nan_id-5:nan_id-1])

        for i, (e, slow) in enumerate(zip(edges, slowdown)):
            print("{}\t{:.0f}".format(i+1, slow))
            print("{}\t{:.0f}".format(i+1, slow), file=open(os.path.join(root, "plots/task4/MM1/", decip), "a+"))

    print("\n------------------\n")
    # set_trace()


def run_pareto():
    print("Exponential M/G/1")
    for decip in ["FCFS", "SJF"]:
        print(decip)
        sim = Simulation(
            params=Params(distribution="pareto", dicipline=decip,
                          C=int(1e5), rho=0.5,
                          lmbd=0.001, mu=1 / 3000))
        sim = sim.run_simulation()
        service_times = [cust.service_time for cust in sim.customers]
        _, edges = np.histogram(service_times, bins=100)
        slowdown = []
        for lo, hi in zip(edges[:-1], edges[1:]):
            slowdown.append(np.mean(np.nan_to_num([cust.wait_time / cust.service_time for cust in
                        sim.customers if lo < cust.service_time <= hi])))
        # set_trace()
        nans = np.where(np.isnan(slowdown))
        slowdown = np.nan_to_num(slowdown)
        for nan_id in nans[0]:
            slowdown[nan_id] = np.mean(slowdown[nan_id-5:nan_id-1])

        for i, (e, slow) in enumerate(zip(edges, slowdown)):
            print("{}\t{:.0f}".format(i+1, slow))
            print("{}\t{:.0f}".format(i+1, slow), file=open(os.path.join(root, "plots/task4/MG1/", decip), "a+"))

        print("\n------------------\n")
    # set_trace()


if __name__ == "__main__":
    # run_pareto()
    run_exponential()
    set_trace()
