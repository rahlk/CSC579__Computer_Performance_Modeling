import click
import logging
from time import time
from time import sleep
from pdb import set_trace
from threading import Thread
from Utils.RandomUtil import Random
from Utils.SimulationUtils import Customer, Server, StoppableThread

logging.basicConfig(level=logging.DEBUG,
                    format='(Queuing Customer %(threadName)s) | %(message)s',)


@click.command()
@click.option('--l', default=0.05, help='Lamdba for the distribution of interarrival times.')
@click.option('--K', default=5, help='The number of customers the server queue may hold.')
@click.option('--C', default=1000, help='Number of customer server before the program terminates.')
@click.option('--L', default=1, help='Any integer such that 1<L<C.')
def main(l, K, C, L):
    set_trace()
    server = Server(K=10)
    customers = []
    current_time = time()
    customer_id = 0
    rand = Random()

    def worker():
        server.service()

    def queuing(id):
        """thread worker function"""
        customer = customers.pop(id)
        customer = server.enqueue(customer)
        customers.insert(id, customer)

    w = Thread(target=worker, name="Service-Thread")
    w.start()

    while len(server.processed) < C:
        next_customer_arrival = rand.exponential(lam=l)
        sleep(next_customer_arrival)
        customer_id += 1
        customers.append(Customer(id=customer_id))
        t = Thread(name = customer_id, target=queuing, args=(customer_id-1,))
        t.start()

    server.kill = True
    set_trace()

if __name__ == '__main__':
    main()
