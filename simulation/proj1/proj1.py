from threading import Thread
from time import time
from time import sleep
import logging
from pdb import set_trace
from Utils import Customer, Server, Random, StoppableThread

logging.basicConfig(level=logging.DEBUG,
                    format='(Queuing Customer %(threadName)s) | %(message)s',)


def main():
    server = Server(K=10)
    customers = []
    current_time = time()
    MAX_CUSTOMERS = 1e4
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
        # print(next_customer_arrival)
        sleep(next_customer_arrival)
        customer_id += 1
        customers.append(Customer(id=customer_id))
        t = Thread(name = customer_id, target=queuing, args=(customer_id-1,))
        t.start()

    server.kill = True

    set_trace()

if __name__ == '__main__':
    main()
