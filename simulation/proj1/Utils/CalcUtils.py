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
