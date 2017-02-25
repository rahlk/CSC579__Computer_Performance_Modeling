from __future__ import division
from __future__ import print_function
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plot
from pdb import set_trace

def histogram(x, N=50, x_label="X", y_label="Y", the_title="Title"):
    # histogram of the data
    n, bins, patches = plot.hist(x, N, normed=1, facecolor="gray", alpha=0.75)
    # add a 'best fit' line
    set_trace()
    z = np.polyfit(N, bins)
    p = np.poly1d(z)
    l = plot.plot(bins, p, 'k--', linewidth=1)

    plot.xlabel(x_label)
    plot.ylabel(y_label)
    plot.title(the_title)

    plot.show()
