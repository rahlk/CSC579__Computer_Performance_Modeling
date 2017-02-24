from __future__ import print_function
from __future__ import division

import os
import sys
from time import time


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
    def __init__(self): pass

    def uniform(self, lo=0, hi=1):
        """
        Uniform distribution
        """
        for 
