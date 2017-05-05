"""
Task 3

Plot average customer waiting time vs. rho (0.1, 0.2, ... , 0.9).
"""

from __future__ import division
from __future__ import print_function

import os
import sys

root = os.path.join(os.getcwd().split("proj3")[0], "proj3")
if not root in sys.path:
    sys.path.append(root)

import numpy as np
from pdb import set_trace
from Utils.SimUtil import Simulation
from Utils.MscUtil import Params
from Utils.StatsUtil import mean_confidence_interval as mci


def run_exponential():
    print("Exponential M/M/m")
    for decip in ["FCFS", "SJF"]:
        print(decip)
        for r in np.arange(0.05, 1, 0.1):
            waits = []
            for n in xrange(10):
                sim = Simulation(
                    params=Params(distribution="exp", dicipline=decip,
                                  C=int(5 * 1e4), rho=r,
                                  lmbd=0.001, mu=1 / 3000))
                sim = sim.run_simulation()
                waits.append(
                    np.median([cust.wait_time for cust in sim.customers]))

            u, u_neg, u_pos = mci(waits, confidence=0.95)
            try:
                print("{}\t{}\t{}\t{}".format(r, int(u), int(u_neg), int(u_pos)))
            except:
                set_trace()

        print("\n------------------\n")


def run_pareto():
    print("Bounded Pareto M/G/m")
    for decip in ["FCFS", "SJF"]:
        print(decip)
        for r in np.arange(0.1, 1, 0.1):
            waits = []
            for n in xrange(10):
                sim = Simulation(
                    params=Params(distribution="pareto", dicipline=decip,
                                  C=int(5 * 1e4), rho=r,
                                  lmbd=0.001, mu=1 / 3000))
                sim = sim.run_simulation()
                waits.append(
                    np.mean([cust.wait_time for cust in sim.customers]))

            u, u_neg, u_pos = mci(waits, confidence=0.95)
            print("{}\t{}\t{}\t{}".format(r, int(u), int(u_neg), int(u_pos)))

        print("\n------------------\n")


if __name__ == "__main__":
    run_exponential()
    run_pareto()
    set_trace()
