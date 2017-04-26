from __future__ import print_function
from __future__ import division

from pdb import set_trace
from Utils.SimUtil import Simulation
from Utils.MscUtil import Params
from numpy import arange

if __name__ == "__main__":

    for r in arange(0.1, 1, 0.1):
        p = Params(distribution="pareto", dicipline="FCFS", C=int(5*1e4), rho=r,
                   lmbd=1 / 3000)
        sim = Simulation(params=p)
        sim = sim.run_simulation()
    set_trace()
