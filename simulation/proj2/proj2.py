from __future__ import print_function
from __future__ import division

from pdb import set_trace
from Utils.SimUtil import Simulation
from Utils.MscUtil import Params

if __name__ == "__main__":

    for r in [0.05, 0.15, 0.25, 0.35]:
        p = Params(K=40, dicipline="FCFS", C=1e5, rho=r, lmbd=1)
        sim = Simulation(params=p)
        sim = sim.run_simulation()
    set_trace()
