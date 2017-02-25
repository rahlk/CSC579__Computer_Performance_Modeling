from __future__ import print_function
from Utils import Random



def __test_rnd():
    rand = Random()
    for _ in xrange(12):
        print(rand.rand0() )

if __name__ == "__main__":
    __test_rnd()
