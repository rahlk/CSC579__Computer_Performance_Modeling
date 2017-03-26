from __future__ import print_function
from __future__ import division

from pdb import set_trace
from Utils.SimUtil import Simulation
from Utils.MscUtil import Params

if __name__ == "__main__":

    p = Params(K=5, dicipline="FCFS", C=1e5, rho = 0.95, lmbd=1)
    sim = Simulation(params=p)
    sim = sim.run_simulation()
    set_trace()
