from __future__ import division
from __future__ import print_function
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plot


def histogram(x, N=50, x_label="X", y_label="Y", the_title="Title"):
    # histogram of the data
    n, bins, patches = plt.hist(x, N, normed=1, facecolor="gray", alpha=0.75)
    # add a 'best fit' line
    set_trace()
    z = np.polyfit(N, bins)
    p = np.poly1d(z)
    l = plt.plot(bins, p, 'k--', linewidth=1)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(the_title)

    plt.show()
