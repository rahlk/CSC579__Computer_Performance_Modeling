from __future__ import print_function
from Utils import Random



def __test_rnd():
    seeds = [1,5,34,98,76,34,56,99]
    for seed in seeds:
        rand = Random()
        rand.set_seed(seed_val=seed)
        for _ in xrange(12):
            print("Seed={seed}|Random={rand_val}".format(seed=seed, rand_val=rand.rand0()))

if __name__ == "__main__":
    __test_rnd()
