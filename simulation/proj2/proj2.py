from __future__ import print_function
from __future__ import division
from Utils.SimUtil import Simulation

if __name__ == "__main__":

    s = Simulation()

    while s.num_serviced < 1000:
        s.advance_time()
        
