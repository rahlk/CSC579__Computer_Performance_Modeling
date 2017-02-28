from __future__ import division
from __future__ import print_function
import numpy as np


def customer_loss_rate(server):
    denied = len(server.rejected)
    total = len(server.rejected + server.processed)
    return denied / total


def mean_service_time(server):
    return np.mean([customer.service_time for customer in server.processed])


def mean_wait_time(server):
    return np.mean([customer.get_wait_time() for customer in server.processed])


def cust_arrival(server, start_time, L):
    return "{}, {}, {}, {}".format(round(server[L].arrival_time-start_time, 2),
                                    round(server[L+1].arrival_time-start_time, 2),
                                    round(server[L+10].arrival_time-start_time, 2),
                                    round(server[L+11].arrival_time-start_time, 2))


def cust_departr(server, L):
    return "{}, {}, {}, {}".format(round(server[L].depart_time-start_time, 2),
                                    round(server[L+1].depart_time-start_time, 2),
                                    round(server[L+10].depart_time-start_time, 2),
                                    round(server[L+11].depart_time-start_time, 2))


def cust_service(server, L):
    pass
