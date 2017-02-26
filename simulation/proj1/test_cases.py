from __future__ import print_function

from Utils.RandomUtil import Random
from Utils.PlotsUtils import histogram


def __test_rand0():
    seeds = [1, 5, 34, 98, 76, 34, 56, 99]
    for seed in seeds:
        rand = Random()
        rand.set_seed(seed_val=seed)
        for _ in xrange(12):
            print("Seed={seed}|Random={rand_val}".format(seed=seed,
                                                         rand_val=rand.rand0()))


def __test_uniform():
    seeds = [1, 5, 34, 98, 76, 34, 56, 99]
    for seed in seeds:
        rand = Random()
        rand.set_seed(seed_val=seed)
        for _ in xrange(12):
            print("Seed={seed} | Random={rand_val}".format(seed=seed,
                                                           rand_val=rand.randint(
                                                               lo=1, hi=10000)))


def __test_randexp():
    seeds = [1, 5, 34, 98, 76, 34, 56, 99]
    for seed in seeds:
        rand = Random()
        rand.set_seed(seed_val=seed)
        for _ in xrange(12):
            print("Seed={seed} | Random={rand_val}".format(seed=seed,
                                                           rand_val=rand.exponential(
                                                               lam=10)))


def __test_histogram():
    seeds = range(0, 30)
    rand = Random()
    x = [rand.rand0() for n in xrange(100000)]
    histogram(x, N=1000)


if __name__ == "__main__":
    __test_histogram()
