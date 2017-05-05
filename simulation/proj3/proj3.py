from __future__ import print_function
from __future__ import division

import argparse
import numpy as np
from Utils.SimUtil import Simulation
from Utils.MscUtil import Params
from pdb import set_trace
from Utils.StatsUtil import mean_confidence_interval as mci
import warnings
warnings.filterwarnings("ignore")


def simulate(l, C, L, M):
    """
    Run simulation of a M//M/1/K queueing system
    """
    print("Parameters:\nC     : {}".format(C))
    print("Lamdba: {}\n".format(l))

    if L == 0:
        decip = "FCFS"
        print("Descipline: FCFS")
    elif L == 1:
        print("Descipline: SJF")
        decip = "SJF"
    else:
        raise ValueError

    if M == 0:
        print("Distribution: Exponential")
        distr = "exp"
    elif M == 1:
        print("Distribution: Bounded Pareto")
        distr = "pareto"
    else:
        raise ValueError

    print("\nRunning simulation ... \n")


    w = []
    s = []

    P = Params(distribution=distr, dicipline=decip,
               C=int(C), rho=0.5,
               lmbd=l, mu=1 / 3000)

    for _ in xrange(4):
        sim = Simulation(params=P).run_simulation()
        w.append(np.mean([cust.wait_time for cust in sim.customers]))
        s.append(np.mean([cust.system_time for cust in sim.customers]))

    """Compute mean and confidence intervals"""
    w_mean, w_neg, w_pos = mci(w, confidence=0.95)
    s_mean, s_neg, s_pos = mci(s, confidence=0.95)

    print(
        "Simulation Details:\nAverage Wait Time    : Mean: {}; Confidence:{}".format(
            round(w_mean, 2), round(1.6 * np.std(w), 2)))
    print("Average System Time  : Mean: {}; Confidence:{}".format(
            round(np.mean(s), 2), round(1.6 * np.std(s), 2)))
    print("Master clock at the end of simulation: {}\n".format(
        round(sim.clock, 2)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--l', default=0.006, type=float,
                        help='Lamdba for the distribution of interarrival '
                             'times.\n DEFAULT --l 0.006.')
    parser.add_argument('--C', default=100000, type=int,
                        help='Number of customed server before the program '
                             'terminates.\n DEFAULT --C 100000')
    parser.add_argument('--L', default=0, type=int,
                        help='Service Decipline. 0-FCFS, 1-SJF')
    parser.add_argument('--M', default=0, type=int,
                        help='Service Type. 0-M/M/3, 1-M/G/3')

    args = parser.parse_args()
    simulate(args.l, args.C, args.L, args.M)
