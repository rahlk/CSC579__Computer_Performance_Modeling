from __future__ import print_function
from __future__ import division
from pdb import set_trace


class Params:
    """
    Set parameters
    """

    def __init__(self, K=5, dicipline="FCFS", C=1e6, rho=0.95, lmbd=1.0, lmbd_disk=0.5, K_io=30):
        self.K = K
        self.C = C
        self.rho = rho
        self.lmbd = lmbd
        self.K_io = K_io
        self.lmbd_disk = lmbd_disk
        self.service_type = dicipline

class Customer:
    """
    Hold's customer data for simulation
    """

    def __init__(self, id):
        self.id = id
        self.q_id = None
        self.re_serve = 0
        self.priority = None
        self.serviced = None
        self.arrival_time = 0
        self.service_time = 0
        self.disk_arrival_time = 0
        self.disk_service_time = 0
        self.depart_time = self.arrival_time
        self.disk_depart_time = self.disk_arrival_time

    def get_wait_time(self):
        self.wait_time = self.depart_time - self.arrival_time + self.service_time
        return self.wait_time

