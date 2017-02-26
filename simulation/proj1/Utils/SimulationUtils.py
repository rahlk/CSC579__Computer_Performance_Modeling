from __future__ import division

import os
import sys
import threading
from pdb import set_trace
from time import time, sleep
from RandomUtil import Random



class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self, target=None, name=None):
        super(StoppableThread, self).__init__(target=target, name=name)
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

class Customer:
    """
    Hold's customer data for simulation
    """

    def __init__(self, id):
        self.id = id
        self.arrival_time = 0
        self.queued = None
        self.in_service = False
        self.serviced = None
        self.denied = None
        self.depart_time = self.arrival_time
        self.service_time = self.arrival_time
        self.wait_time = self.depart_time - self.arrival_time - self.service_time


class Server:
    """
    Simulate a Server
    """

    def __init__(self, K):
        self.queue_size = K
        self.queue = []
        self.rand = Random()
        self.processed = []
        self.rejected = []
        self.kill = False

    def get_service_time(self):
        return self.rand.exponential(lam=1)

    def enqueue(self, customer):
        current_time = time()
        customer.arrival_time = current_time
        if len(self.queue) < self.queue_size:
            self.queue.append(customer)
            customer.queued = True
        else:
            customer.queued = False
            customer.denied = True
            customer.depart_time = current_time
            self.rejected.append(customer)

        return customer

    def dequeue(self, customer):
        for customer_postion, queued_customer in enumerate(self.queue):
            if queued_customer.id == customer.id:
                return self.queue.pop(customer_postion)

    def service(self):
        while not self.kill:
            for next_customer in self.queue:
                next_customer.in_service = True
                service_time = self.get_service_time()
                sleep(service_time)
                next_customer.serviced = True
                next_customer.service_time = service_time
                next_customer.depart_time = time()
                self.processed.append(self.dequeue(next_customer))
