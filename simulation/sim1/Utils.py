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
        self.idum = 0
        self.mask = 123459876


    def seed(self, val=1):
        self.seed = val


    def rand0(self, idum=0):
        """
        Uniform distribution
        """
        self.idum = idum if not self.idum == idum else self.idum
        self.idum = int(hex(self.idum) & hex(self.mask), 16)
        set_trace()
        k = self.idum / self.iq
        self.idum = self.ia * (self.idum - k*self.iq) - self.ir * k
        if self.idum <0:
            self.idum += self.im
        ans = self.am * self.idum
        self.idum ^= self.mask
        return ans
