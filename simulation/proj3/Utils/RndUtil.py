from __future__ import division
from numpy import log, mean, std


class Random:
    """
    Defines custom random number generator
    """

    def __init__(self):

        self.ia = 16807
        self.im = 2147483647
        self.am = (1.0 / self.im)
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
        self.idum = long(self.ia * (self.idum - k * self.iq) - self.ir * k)
        if self.idum < 0:
            self.idum += self.im
        ans = self.am * self.idum
        return ans

    def uniform(self, lo=0, hi=1):
        return lo + (hi - lo) * self.rand0()

    def int(self, lo=0, hi=100):
        return int(self.uniform(lo, hi))

    def exponential(self, lam=1/3000, idnum=None):

        if idnum is not None:
            self.set_seed(idnum)

        dummy = 0
        while dummy == 0:
            dummy = self.rand0(idnum)

        return -log(dummy) / lam

    def bounded_pareto(self, a=1.1, k=332, p=10e10, idnum=None):

        if idnum is not None:
            self.set_seed(idnum)

        dummy = 0
        while dummy == 0:
            dummy = self.rand0(idnum)

        return ((p**a+dummy*k**a-dummy*p**a)/((p*k)**a))**-(1/a)

if __name__ == "__main__":
    from pdb import set_trace
    rand = Random()
    rand.set_seed(seed_val=1729)
    a = [rand.bounded_pareto() for _ in xrange(100000)]
    set_trace()
