from __future__ import print_function
from __future__ import division

import os
import sys
from time import time
from pdb import set_trace

class Customer:
    """
    Hold's customer data for simulation
    """
    def __init__(self):
        self.arrival_time = time()
        self.queued = False
        self.serviced = False
        self.depart_time = self.arrival_time
        self.service_time = self.arrival_time-self.depart_time


class Random:
    """
    Defines custom random number generator
    """
    def __init__(self):

        self.ia = 16807
        self.im = 2147483647
        self.am = (1.0/self.im)
        self.iq = 127773
        self.ir = 2836
        self.idum = 12458
        self.mask = 123459876


    def set_seed(self, seed_val=1):
        self.idum = seed_val


    def rand0(self):
        """
        Uniform distribution
        """
        self.idum = long(self.idum ^ self.mask)
        k = long(self.idum / self.iq)
        self.idum = long(self.ia * (self.idum - k*self.iq) - self.ir * k)
        if self.idum <0:
            self.idum += self.im
        ans = self.am * self.idum
        return ans

    def rand_exp():
        pass
