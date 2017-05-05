from __future__ import division, print_function

import numpy as np
import scipy as sp
import scipy.stats


def mean_confidence_interval(data, confidence=0.95):
    for i, d in enumerate(data):
        if np.isnan(d):
            data[i] = data[i - 1] * 0.5 + data[i + 1] * 0.5

    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * sp.stats.t._ppf((1 + confidence) / 2., n - 1)
    return m, 0.5 * abs(m - h), 0.5 * abs(m + h)
