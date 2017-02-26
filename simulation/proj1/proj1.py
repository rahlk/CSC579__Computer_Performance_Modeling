import argparse
import logging
from time import time
from time import sleep
from pdb import set_trace
from threading import Thread
from Utils.RandomUtil import Random
from Utils.ServerUtil import Customer, Server
from Utils.MisclUtils import StoppableThread
from Utils.PlotsUtils import histogram

logging.basicConfig(level=logging.DEBUG,
                    format='(Queuing Customer %(threadName)s) | %(message)s',)


def main(l, server_lim, MAX_SERVICED, L, verbose):
    # set_trace()
    server = Server(K=server_lim)
    customers = []
    current_time = time()
    customer_id = 0
    rand = Random()

    def worker():
        last_served = server.service(verbose)


    def queuing(id):
        """thread worker function"""
        customer = customers.pop(id)
        customer = server.enqueue(customer)
        customers.insert(id, customer)
        if verbose: logging.debug('Accepted: {}'.format(customer.queued))

    w = Thread(target=worker, name="Service-Thread")
    w.start()

    while len(server.processed) < MAX_SERVICED:
        next_customer_arrival = rand.exponential(lam=l)
        sleep(next_customer_arrival)
        customer_id += 1
        customers.append(Customer(id=customer_id))
        t = Thread(name = customer_id, target=queuing, args=(customer_id-1,))
        t.start()

    server.kill = True
    set_trace()

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--l', default=0.85, help='Lamdba for the distribution of interarrival times.')
    parser.add_argument('--K', default=5, help='The number of customers the server queue may hold.')
    parser.add_argument('--C', default=1000, help='Number of customer server before the program terminates.')
    parser.add_argument('--L', default=1, help='Any integer such that 1<L<C.')
    parser.add_argument('-V', '--verbosity', default=0, help='Verbose mode. Print debug log.')

    args = parser.parse_args()
    main(args.l, args.K, args.C, args.L, args.verbosity)
