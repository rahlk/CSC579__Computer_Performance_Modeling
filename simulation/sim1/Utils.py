from __future__ import print_function
from __future__ import division

import os
import sys
from time import time
from pdb import set_trace
from numpy import log

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
        self.idum = long(seed_val)


    def rand0(self, idnum=None):
        """
        Uniform distribution
        """
        if idnum is not None:
            self.set_seed(idnum)

        self.idum = long(self.idum ^ self.mask)
        k = long(self.idum / self.iq)
        self.idum = long(self.ia * (self.idum - k*self.iq) - self.ir * k)
        if self.idum <0:
            self.idum += self.im
        ans = self.am * self.idum
        return ans


    def uniform(self, lo=0, hi=1):
        return lo + (hi-lo)*self.rand0()


    def randint(self, lo=0, hi=100):
        return int(self.uniform(lo, hi))


    def randexp(self, lambda=1, idnum=None):

        if idnum is not None:
            self.set_seed(idnum)

        dummy = 0
        while dummy == 0:
            dummy = self.rand0(idnum)

        return -log(dummy)/lambda
