from __future__ import print_function
from __future__ import division

import argparse
import numpy as np
from pdb import set_trace
from Utils.SimUtil import Simulation
from Utils.MscUtil import Params


def simulate(l, C, L, M):
    """
    Run simulation of a M//M/1/K queueing system
    """
    print("Parameters:\nC     : {}".format(C))
    print("Lamdba: {}\n".format(l))
    print("Running simulation ... \n")

    if L == 0:
        decip = "FCFS"
    elif L == 1:
        decip = "SJF"

    if M == 0:
        distr = "exp"
    elif M == 1:
        distr = "pareto"

    w = []
    s = []

    P = Params(distribution=distr, dicipline=decip,
               C=int(C), rho=0.5,
               lmbd=l, mu=1 / 3000)

    for _ in xrange(4):
        sim = Simulation(params=P).run_simulation()

        s.append(np.mean([cust.wait_time for cust in sim.customers]))
        w.append(np.mean([cust.get_wait_time() for cust in sim.customers]))

    print(
        "Simulation Details:\nAverage Wait Time    : Mean: {}; Confidence:{}".format(
            round(np.mean(w), 2), round(1.6 * np.std(w), 2)))
    print(
        "Simulation Details:\nAverage System Time    : Mean: {}; Confidence:{}".format(
            round(np.mean(s), 2), round(1.6 * np.std(w), 2)))
    print("Master clock at the end of simulation: {}\n".format(
        round(sim.clock, 2)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--l', default=0.05, type=float,
                        help='Lamdba for the distribution of interarrival '
                             'times.\n DEFAULT --l 0.85.')
    parser.add_argument('--C', default=100000, type=int,
                        help='Number of customed server before the program '
                             'terminates.\n DEFAULT --C 100000')
    parser.add_argument('--L', default=0, type=int,
                        help='Service Decipline. 0-FCFS, 1-SJF')
    parser.add_argument('--M', default=0, type=int,
                        help='Service Type. 0-M/M/3, 1-M/G/3')

    args = parser.parse_args()
    simulate(args.l, args.C, args.L, args.M)
