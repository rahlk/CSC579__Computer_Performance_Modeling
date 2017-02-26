import logging
from time import time
from time import sleep
from pdb import set_trace
from threading import Thread
from Utils.RandomUtil import Random
from Utils.SimulationUtils import Customer, Server, StoppableThread

logging.basicConfig(level=logging.DEBUG,
                    format='(Queuing Customer %(threadName)s) | %(message)s',)


def main():
    server = Server(K=10)
    customers = []
    current_time = time()
    MAX_CUSTOMERS = 1e2
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

    while len(customers) < MAX_CUSTOMERS:
        next_customer_arrival = rand.exponential(lam=0.05)
        sleep(next_customer_arrival)
        customer_id += 1
        customers.append(Customer(id=customer_id))
        t = Thread(name = customer_id, target=queuing, args=(customer_id-1,))
        t.start()

    server.kill = True
    set_trace()

if __name__ == '__main__':
    main()
