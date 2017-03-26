from __future__ import print_function
from __future__ import division

class Params:
    def __init__(self, K=5, dicipline="FCFS", C=1e6, rho=0.95, lmbd=1.0):
        """
        Set parameters
        """
        self.K = K
        self.C = C
        self.rho = rho
        self.lmbd = lmbd
        self.service_type = dicipline
