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


    def seed(self, val=1):
        self.seed = val


    def rand0(self):
        """
        Uniform distribution
        """
        # self.idum = idum if not self.idum == idum else self.idum
        self.idum = long(self.idum ^ self.mask)
        print("idum={}".format(self.idum))
        k = long(self.idum / self.iq)
        print("k={}".format(k))
        self.idum = long(self.ia * (self.idum - k*self.iq) - self.ir * k)
        if self.idum <0:
            self.idum += self.im
        ans = self.am * self.idum
        # self.idum = self.idum ^ self.mask
        return ans
