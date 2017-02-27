from __future__ import division

import os
import sys
from pdb import set_trace
from RandomUtil import Random
from MisclUtils import TimeUtil


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

    def get_wait_time(self):
        self.wait_time = self.depart_time - self.arrival_time - self.service_time
        return self.wait_time


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
        self.timer = TimeUtil()

    def get_service_time(self):
        return self.rand.exponential(lam=1)

    def enqueue(self, customer):
        current_time = self.timer.current_time()
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

    def service(self, verbose=False):
        while not self.kill:
            for next_customer in self.queue:
                next_customer.in_service = True
                service_time = self.get_service_time()
                self.timer.wait_millisc(service_time)
                next_customer.serviced = True
                next_customer.service_time = service_time
                next_customer.depart_time = self.timer.current_time()
                last_served = self.dequeue(next_customer)
                self.processed.append(last_served)
                if verbose:
                    print("(Serving Customer {}) | Remaining: {}".format(
                        last_served.id, self.queue_size - len(self.queue)))
