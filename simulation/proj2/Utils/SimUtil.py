from __future__ import print_function
from __future__ import division
from RndUtil import Random
from pdb import set_trace
from MscUtil import Params, Customer

rand = Random()
rand.set_seed(seed_val=1729)

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
        self.priority_queue = {"1": list(), "2": list(), "3": list(),
                               "4": list()}
        self.params = params
        self.customers = list()
        self.t_depart = float('inf')
        self.num_in_system = len(self.queue)
        self.t_arrive = self.generate_interarrival()

        self.clock = 0
        self.num_arrive = 0
        self.num_depart = 0
        self.num_reject = 0
        self.num_serviced = 0
        self.total_wait = sum([c.get_wait_time() for c in self.customers])

    @staticmethod
    def random_queue():
        random = rand.uniform()
        if 0 < random < 0.25:
            return "1"
        elif 0.25 < random < 0.5:
            return "2"
        elif 0.5 < random < 0.75:
            return "3"
        elif 0.75 < random < 1:
            return "4"

    @staticmethod
    def all_empty(queue):
        sizes = [len(q) for _, q in queue.iteritems()]
        return sum(sizes) == 0

    def generate_interarrival(self):
        return rand.exponential(self.params.rho)

    def generate_service_time(self):
        return rand.exponential(self.params.lmbd)

    def prioritize(self):

        if self.params.service_type == "FCFS":
            for k, _ in enumerate(self.queue):
                c = self.queue[k]
                c.priority = k
                self.queue[k] = c

            return self.queue

        elif self.params.service_type == "LCFS":
            for k, _ in enumerate(self.queue):
                c = self.queue[k]
                c.priority = len(self.queue) - k
                self.queue[k] = c

            return self.queue

        elif self.params.service_type == "SJF":

            sorted_args = sorted(self.queue, key=lambda X: X.service_time)

            def find(n):
                for i, c in enumerate(self.queue):
                    if c == n:
                        return i

            for k, n in enumerate(sorted_args):
                c = self.queue[find(n)]
                c.priority = k
                self.queue[find(n)] = c

            return self.queue

    def handle_arrive_event(self):
        self.num_arrive += 1  # Increment arrival
        c = Customer(id=self.num_arrive)
        self.t_arrive = self.clock + self.generate_interarrival()
        c.arrival_time = self.t_arrive

        #  If the queue is full kick out the customer
        if len(self.queue) >= self.params.K:
            c.depart_time = c.arrival_time
            self.t_depart = c.depart_time
            self.num_reject += 1
            c.serviced = False
            self.customers.append(c)

        # Else add to queue
        else:
            c.serviced = True
            c.service_time = self.generate_service_time()
            self.queue.append(c)
            self.queue = self.prioritize()

    def handle_depart_event(self):
        self.num_depart += 1
        if len(self.queue) > 0:
            self.num_serviced += 1
            sorted_queue = sorted(self.queue, key=lambda C: C.priority)
            c = sorted_queue.pop(0)
            c.depart_time = self.clock + c.service_time
            self.t_depart = c.depart_time
            self.customers.append(c)
            self.queue = [c for c in self.queue if c in sorted_queue]
        else:
            self.t_depart = float("inf")

    def handle_multiqueue_arrive(self):
        self.num_arrive += 1  # Increment arrival
        c = Customer(id=self.num_arrive)
        self.t_arrive = self.clock + self.generate_interarrival()
        c.arrival_time = self.t_arrive

        q_id = self.random_queue()
        #  If the queue is full kick out the customer
        if len(self.priority_queue[q_id]) >= self.params.K / 4:
            c.depart_time = c.arrival_time
            self.t_depart = c.depart_time
            self.num_reject += 1
            c.serviced = False
            self.customers.append(c)

        # Else add to queue
        else:
            c.serviced = True
            c.service_time = self.generate_service_time()
            c.q_id = q_id
            self.priority_queue[q_id].append(c)

    def handle_multiqueue_depart(self):
        self.num_depart += 1
        for q_id, queue in self.priority_queue.iteritems():
            if len(queue) > 0:
                self.num_serviced += 1
                c = queue.pop(0)
                c.depart_time = self.clock + c.service_time
                self.t_depart = c.depart_time
                self.customers.append(c)
                break

        if self.all_empty(self.priority_queue):
            self.t_depart = float("inf")

    def advance_time(self):
        self.clock = min(self.t_arrive, self.t_depart)
        if self.t_arrive < self.t_depart:
            if self.params.service_type == "PrioNP" \
                    or self.params.service_type == "PrioP":

                self.handle_multiqueue_arrive()

            else:
                self.handle_arrive_event()
        else:
            if self.params.service_type == "PrioNP" \
                    or self.params.service_type == "PrioP":

                self.handle_multiqueue_depart()

            else:
                self.handle_depart_event()

    def run_simulation(self):
        while self.num_depart < self.params.C:
            self.advance_time()

        return self
