"""
Single Server M/M/1 and M/G/1
"""

from __future__ import print_function
from __future__ import division
from RndUtil import Random
from pdb import set_trace
from MscUtil import Params, Customer
from numpy.random import shuffle
from numpy import argsort, mean
rand = Random()
rand.set_seed(seed_val=1729)
from time import time
"""
Why 1729?
Well, it is a very interesting number.
It is the smallest number expressible as the sum of two positive cubes in
two different ways.
"""


class Simulation:
    def __init__(self, params=Params):

        "Initialize inital params"
        self.queue = list()
        self.params = params
        self.customers = list()
        self.t_arrive = self.generate_interarrival()
        self.t_depart = self.t_arrive
        self.num_in_system = len(self.queue)
        self.t_fin_1 = 0
        self.t_fin_2 = 0
        self.t_fin_3 = 0

        self.clock = 0
        self.num_arrive = 0
        self.num_depart = 0
        self.num_reject = 0
        self.num_serviced = 0
        self.total_wait = sum([c.get_wait_time() for c in self.customers])

    def generate_interarrival(self):
        return rand.exponential(3*self.params.rho/(len(self.queue)+1e-32))

    def generate_service_time(self):
        if self.params.distribution == "exp":
            return rand.exponential(self.params.mu)
        else:
            service_time = rand.bounded_pareto()
            return service_time

    def _server(self, c):
        self.num_serviced += 1
        self.t_fin_1 = self.clock + c.service_time
        self.t_depart = self.t_fin_1
        c.depart_time = self.t_depart
        c.system_time = self.t_depart - c.arrival_time
        c.wait_time = self.t_depart - c.arrival_time + c.service_time
        self.t_fin_1 = 0
        return c

    def handle_arrive_event(self):
        self.num_arrive += 1  # Increment arrival
        c = Customer(id=self.num_arrive)
        c.arrival_time = self.clock
        c.service_time = self.generate_service_time()
        self.t_arrive = self.clock + self.generate_interarrival()
        self.queue.append(c)

    def handle_depart_event(self):
        if len(self.queue) > 0:
            if self.params.service_type == "FCFS":
                c = self.queue.pop(0)
            else:
                serv_times = [c.service_time for c in self.queue]
                sorted_serve_time = argsort(serv_times)
                c = self.queue.pop(sorted_serve_time[0])

            c = self._server(c)
            self.customers.append(c)

        else:
            self.t_depart = self.t_arrive

    def advance_time(self):
        self.clock = min(self.t_arrive, self.t_depart)
        if self.t_arrive <= self.t_depart:
            self.handle_arrive_event()
        else:
            self.handle_depart_event()

    def run_simulation(self):

        while self.num_arrive < self.params.C:
            self.advance_time()


        return self
