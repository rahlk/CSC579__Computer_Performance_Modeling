"""
Task 2

Plot average customer waiting time vs. rho (0.05, 0.15, ... , 0.95).
"""

from __future__ import print_function
from __future__ import division
import os, sys

root = os.path.join(os.getcwd().split("proj2")[0], "proj2")
if not root in sys.path:
    sys.path.append(root)

import numpy as np
import pandas as pd
from pdb import set_trace
from Utils.SimUtil import Simulation
from Utils.MscUtil import Params

if __name__ == "__main__":

    for decip in ["SJF", "LCFS", "FCFS"]:
        print(decip)
        for r in np.arange(0.05,1,0.1):
            waits = []
            for _ in xrange(10):
                sim = Simulation(params = Params(K=40, dicipline=decip, C=1e5, rho = r, lmbd=1))
                sim = sim.run_simulation()
                waits.append(np.mean([cust.get_wait_time() for cust in sim.customers]))
            print("{}\t{}\t{}\t{}".format(r, np.mean(waits),
                                      np.mean(waits)-1.6*np.std(waits),
                                      np.mean(waits)+1.6*np.std(waits)))
        print("\n------------------\n")

    set_trace()
