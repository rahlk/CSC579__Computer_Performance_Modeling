from __future__ import print_function
from __future__ import division

from pdb import set_trace
from Utils.SimUtil import Simulation


if __name__ == "__main__":

    sim = Simulation()
    sim = sim.run_simulation(C=1e5)
    set_trace()
