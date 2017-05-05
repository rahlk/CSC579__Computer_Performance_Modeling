from __future__ import print_function
from __future__ import division
from RndUtil import Random
from MscUtil import Params, Customer
from numpy.random import shuffle
from numpy import argsort, mean

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
        self.clock = 0
        self.t_fin_1 = 0
        self.t_fin_2 = 0
        self.t_fin_3 = 0
        self.num_arrive = 0
        self.num_serviced = 0

        self.queue = list()
        self.params = params
        self.customers = list()
        self.t_arrive = self.__generate_interarrival()
        self.t_depart = self.t_arrive

    def __generate_interarrival(self):
        return rand.exponential(self.params.lmbd)

    def __generate_service_time(self):
        if self.params.distribution == "exp":
            return rand.exponential(self.params.mu)
        else:
            service_time = rand.bounded_pareto()
            return service_time

    def __compute_wait_times(self):
        for i, _ in enumerate(self.customers[1:]):
            c = self.customers[i]
            c.wait_time = self.customers[i - 1].depart_time - self.customers[i].depart_time
            self.customers.pop(i)
            self.customers.insert(i, c)

    def __next_queue_element(self):
        if self.params.service_type == "FCFS":
            return 0
        else:
            serv_times = [c.service_time for c in self.queue]
            sorted_serve_time = argsort(serv_times)
            return sorted_serve_time[0]

    def __server_1(self, c):
        self.num_serviced += 1
        self.t_fin_1 = self.clock
        c.depart_time = self.t_depart
        self.t_fin_1 = 0
        return c

    def __server_2(self, c):
        self.num_serviced += 1
        self.t_fin_2 = self.clock
        c.depart_time = self.t_depart
        self.t_fin_2 = 0
        return c

    def __server_3(self, c):
        self.num_serviced += 1
        self.t_fin_3 = self.clock
        c.depart_time = self.t_depart
        self.t_fin_3 = 0
        return c

    def __handle_arrive_event(self):
        self.num_arrive += 1  # Increment arrival
        c = Customer(id=self.num_arrive)  # Create customer
        c.arrival_time = self.clock  # Set customer arrival time
        c.service_time = self.__generate_service_time()  # Generate customer service time
        self.t_arrive = self.clock + self.__generate_interarrival()  # Next customer arrival time
        c.wait_time = abs(
            c.service_time + self.t_arrive - self.t_depart) / 3  # Compute mean wait time of the customer (#servers=3)
        c.system_time = abs(self.t_arrive - self.t_depart) / 3  # Compute mean wait time of the customer (#servers=3)
        self.queue.append(c)  # Append the current customer to the queue
        self.t_depart = self.queue[self.__next_queue_element()].service_time + self.clock

    def __handle_depart_event(self):
        if len(self.queue) > 0:
            " If there are customers in the queue"
            next_queue_id = self.__next_queue_element()  # Select the next customer (based on service discipline)
            c = self.queue.pop(next_queue_id)  # Obtain the next customer
            servers = [
                (self.__server_1, self.t_fin_1),
                (self.__server_2, self.t_fin_2),
                (self.__server_3, self.t_fin_3)
            ]
            if self.t_fin_1 == self.t_fin_2 == self.t_fin_3 == 0:  # If all servers are idle, then pick one at random
                shuffle(servers)
                next_server = servers[0]
            else:
                next_server = sorted(servers, key=lambda X: X[1])[0]  # Else, pick the next idle server.

            c = next_server[0](c)  # Process the customers
            self.customers.append(c)
        else:
            "If the queue is empty, then there's no depart event"
            self.t_depart = self.t_arrive

    def __advance_time(self):
        self.clock = min(self.t_arrive, self.t_depart)  # Get next event.

        if self.t_arrive <= self.t_depart:
            "If arrive event call the arrive routine."
            self.__handle_arrive_event()
        else:
            "Else call the depart routine."
            self.__handle_depart_event()

    def run_simulation(self):

        while self.num_arrive < self.params.C:
            self.__advance_time()

        return self
