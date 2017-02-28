import argparse
import logging
from pdb import set_trace
from threading import Thread
from Utils.MisclUtils import TimeUtil
from Utils.RandomUtil import Random
from Utils.ServerUtil import Customer, Server

logging.basicConfig(level=logging.DEBUG,
                    format='(Queuing Customer %(threadName)s) | %(message)s', )

timer = TimeUtil()

def simulate(l, server_lim, max_serviced, L, verbose):
    """
    Run simulation of a M//M/1/K queueing system

    :param l: Lamdba for the distribution of interarrival
    :param server_lim: The number of customers the server queue may hold
    :param max_serviced: Number of customer served before the program terminates
    :param L: Any integer such that 1<L<C
    :param verbose: Print debug log
    :return: customers: List of populated Customer objects.
    """

    server = Server(K=server_lim)
    customers = []
    customer_id = 0
    rand = Random()
    start_time = timer.current_time()
    rand.set_seed(seed_val=12458)


    def worker():
        last_served = server.service(verbose)

    def queuing(customer):
        """
        Dispatch incoming requests to queues
        """
        customer = server.enqueue(customer)
        customers.append(customer)
        if verbose: logging.debug('Accepted: {} | Customers: {}'.format(customer.queued, len(customers)))



    w = Thread(target=worker, name="Service-Thread")
    w.start()

    while len(server.processed) < max_serviced:
        next_customer_arrival = rand.exponential(lam=l)
        timer.wait_millisc(next_customer_arrival)
        customer_id += 1
        t = Thread(name=customer_id, target=queuing, args=(Customer(id=customer_id),))
        t.start()

    server.kill = True
    end_time = timer.current_time()


    if verbose:
        print("Lamdba: {}".format(l))
        print("K     : {}".format(server_lim))
        print("C     : {}".format(max_serviced))
        print("Master clock at the end of simulation: {}".format(int(end_time-start_time)))
        # print("Customer Loss Rate: {}")
        # print("Average Service Time: {}")
        # print("Average Wait Time: {}")
        # print("Lamdba: {}")
    return server


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--l', default=0.85, type=float,
                        help='Lamdba for the distribution of interarrival '
                             'times.\n DEFAULT --l 0.85.')
    parser.add_argument('--K', default=5,
                        help='The number of customers the server queue may '
                             'hold.\n DEFAULT --K 5.')
    parser.add_argument('--C', default=1000,
                        help='Number of customed server before the program '
                             'terminates.\n DEFAULT --C 1000')
    parser.add_argument('--L', default=1,
                        help='Any integer such that 1<L<C.\n DEFAULT --L 1')
    parser.add_argument('-v', '--debug', action='store_true', default=0,
                        help='Verbose mode. Print debug log.')

    args = parser.parse_args()
    simulate(args.l, args.K, args.C, args.L, args.debug)
