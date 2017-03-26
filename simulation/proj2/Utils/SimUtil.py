from __future__ import print_function
from __future__ import division
from RndUtil import Random
from pdb import set_trace

rand = Random()
rand.set_seed(seed_val=1729)
"""
Why 1729?
Well, it is a very interesting number; it is the smallest number expressible as the sum of two positive cubes in two different ways.
"""


class Params:
    K=5

class Customer:
    """
    Hold's customer data for simulation
    """

    def __init__(self, id):
        self.id = id
        self.arrival_time = 0
        self.queued = None
        self.priority = None
        self.in_service = False
        self.serviced = None
        self.depart_time = self.arrival_time
        self.service_time = 0

    def get_wait_time(self):
        self.wait_time = self.depart_time - self.arrival_time + self.service_time
        return self.wait_time



class Simulation:
    def __init__(self, params=Params):

        "Initialize inital params"
        self.queue = list()
        self.customers = list()
        self.t_depart = float('inf')
        self.t_arrive = self.generate_interarrival()
        self.num_in_system = len(self.queue)

        self.rho = 1.
        self.clock = 0
        self.lamdba = 0.95
        self.num_arrive = 0
        self.num_depart = 0
        self.num_reject = 0
        self.num_serviced = 0
        self.total_wait = sum([c.get_wait_time() for c in self.customers])

        self.params = params if params else Params


    @staticmethod
    def generate_interarrival(l=1):
        return rand.exponential(l)

    @staticmethod
    def generate_service_time(l=1):
        return rand.exponential(l)


    def handle_arrive_event(self):
        self.num_arrive += 1  #  Increment arrival
        c = Customer(id=self.num_arrive)
        self.t_arrive = self.clock + self.generate_interarrival(self.lamdba)
        c.arrival_time = self.t_arrive

        #  If the queue is full kick out the customer
        if len(self.queue) >= self.params.K:
            c.depart_time = c.arrival_time
            self.t_depart = c.depart_time
            self.num_reject += 1
            c.serviced = False
            c.priority = self.params.K-len(self.queue)
            self.customers.append(c)

        else:  #  Else add to queue
            c.serviced = True
            self.queue.append(c)

    def handle_depart_event(self):
        self.num_depart += 1
        if len(self.queue) > 0:
            self.num_serviced += 1
            c = self.queue.pop(0)
            c.service_time = self.generate_service_time(self.rho)
            c.depart_time = self.clock + c.service_time
            self.t_depart = c.depart_time
            self.customers.append(c)
        else:
            self.t_depart = float("inf")

    def advance_time(self):
        self.clock = min(self.t_arrive, self.t_depart)
        if self.t_arrive < self.t_depart:
            self.handle_arrive_event()
        else:
            self.handle_depart_event()

    def run_simulation(self, C=1e5):
        while self.num_serviced < C:
            self.advance_time()

        return self
