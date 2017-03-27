from __future__ import print_function
from __future__ import division
from RndUtil import Random
from pdb import set_trace
from MscUtil import Params, Customer

rand = Random()
rand.set_seed(seed_val=1729)


class WebServer:
    def __init__(self, params=Params):

        "Initialize inital params"
        self.cpu__queue = list()
        self.disk_queue = {
            "Disk 1": list(),
            "Disk 2": list(),
            "Disk 3": list()
        }
        self.params = params
        self.customers = list()
        self.t_depart = float('inf')
        self.t_disk_depart = float('inf')
        self.num_in_system = len(self.queue)
        self.t_arrive = self.generate_interarrival()
        self.t_disk_arrive = self.generate_interarrival()

        self.clock = 0
        self.num_serviced = 0
        self.num_cpu__depart = 0
        self.num_cpu__arrive = 0
        self.num_cpu__reject = 0
        self.num_disk_depart = 0
        self.num_disk_arrive = 0
        self.num_disk_reject = 0
        self.total_wait = sum([c.get_wait_time() for c in self.customers])

    @staticmethod
    def random_queue():
        random = rand.uniform()
        if 0 <= random < 0.1:
            return "Disk 1"
        elif 0.1 <= random < 0.2:
            return "Disk 2"
        elif 0.2 <= random < 0.3:
            return "Disk 3"
        elif 0.3 <= random < 1:
            return "exit_system"

    @staticmethod
    def all_empty(queue):
        sizes = [len(q) for _, q in queue.iteritems()]
        return sum(sizes) == 0

    def generate_interarrival(self):
        return rand.exponential(self.params.rho)

    def generate_service_time(self):
        return rand.exponential(self.params.lmbd)

    def generate_disk_service(self):
        return rand.exponential(self.params.lmdb_disk)

    def disk_arrive_event(self, c, disk):
        self.num_disk_arrive += 1  # Increment arrival
        self.t_disk_arrive = (disk, c.depart_time)

        #  If the queue is full kick out the customer
        if len(self.disk_queue[disk]) >= self.params.K_io:
            c.disk_depart_time = c.disk_arrival_time
            self.t_disk_depart = c.disk_depart_time
            self.num_disk_reject += 1
            c.serviced = False
            self.customers.append(c)

        # Else add to queue
        else:
            c.serviced = True
            c.disk_service_time = self.generate_disk_service()
            self.disk_queue[disk].append(c)

    def disk_depart_event(self, disk):
        self.num_disk_depart += 1
        if len(self.disk_queue[disk]) > 0:
            c = self.disk_queue[disk].pop(0)
            c.disk_depart_time = self.clock + c.disk_service_time
            self.t_disk_depart = (disk, c.disk_depart_time)
            self.handle_cpu_arrive(c)
        else:
            self.t_disk_depart = float("inf")

    def handle_cpu_arrive(self, c=None):
        self.num_cpu__arrive += 1  # Increment arrival

        if c is None:  # New arrival
            c = Customer(id=self.num_cpu__arrive)
            self.t_arrive = self.clock + self.generate_interarrival()
            c.arrival_time = self.t_arrive
        else:  # Arrival from a disk
            c.re_serve += 1
            self.t_arrive = c.disk_depart_time
            c.arrival_time = self.t_arrive

        # If the queue is full kick out the customer
        if len(self.queue) >= self.params.K_cpu:
            c.depart_time = c.arrival_time
            self.t_depart = ("exit_system", c.depart_time)
            self.num_reject += 1
            c.serviced = False
            self.customers.append(c)

        # Else add to queue
        else:
            c.serviced = True
            c.service_time = self.generate_service_time()
            self.cpu__queue.append(c)

    def handle_cpu_depart(self):
        self.num_depart += 1

        if len(self.cpu__queue) > 0:  # Process CPU queue
            self.num_serviced += 1
            c = self.cpu__queue.pop(0) # Remove the first customer
            to_disk = self.random_queue() # Determine if she/he needs to be sent to disk
            c.depart_time = self.clock + c.service_time # Get cpu service time

            if to_disk == "exit_system": # If customer leaves the system
                self.customers.append(c)
                self.t_depart = (to_disk, c.depart_time)
            else: # Send to I/O disk
                self.disk_arrive_event(c, disk=to_disk)

        else:
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
        while self.num_serviced < self.params.C:
            self.advance_time()

        return self
