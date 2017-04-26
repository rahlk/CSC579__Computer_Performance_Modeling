from __future__ import print_function
from __future__ import division
from pdb import set_trace


class Params:
    """
    Set parameters
    """

    def __init__(self, dicipline, distribution="exp", C=1e6, rho=0.95,
                 lmbd=1.0, mu=1/3000):
        self.C = C
        self.mu = mu
        self.rho = rho
        self.lmbd = lmbd
        self.service_type = dicipline
        self.distribution = distribution


class Customer:
    """
    Hold's customer data for simulation
    """

    def __init__(self, id):
        self.id = id
        self.arrival_time = 0
        self.service_time = 0
        self.wait_time = 0
        self.depart_time = self.arrival_time

    def get_system_time(self):
        self.wait_time = self.depart_time - self.arrival_time
        return self.wait_time

    def get_wait_time(self):
        self.wait_time = self.depart_time - self.arrival_time + self.service_time
        return self.wait_time
