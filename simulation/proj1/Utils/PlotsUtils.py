from __future__ import division
from __future__ import print_function
import numpy as np
import matplotlib.style
import matplotlib.mlab as mlab
import matplotlib.pyplot as plot
from pdb import set_trace


def line(x, y, x_label="X", y_label="Y", the_title="Title"):
    """
    Plot a histogram of the data
    """

    plot.style.use('fivethirtyeight')
    plot.rcParams["font.family"] = "monospace"

    plot.plot(x, y, linewidth=2)

    plot.xlabel(x_label)
    plot.ylabel(y_label)
    plot.title(the_title)
    plot.show()

def line2(x, y, x_1, y_1, x_label="X", y_label="Y", the_title="Title"):
    """
    Plot a histogram of the data
    """

    plot.style.use('fivethirtyeight')
    plot.rcParams["font.family"] = "monospace"

    plot.plot(x, y, "r", x_1, y_1, 'k', linewidth=2)

    plot.xlabel(x_label)
    plot.ylabel(y_label)
    plot.title(the_title)
    plot.show()

def histogram(x, axis=None, N=50, x_label="X", y_label="Y", the_title="Title"):
    """
    Plot a histogram of the data
    """
    if axis is not None:
        N = len(axis)

    plot.style.use('fivethirtyeight')
    plot.rcParams["font.family"] = "monospace"

    n, bins, patches = plot.hist(x, N, facecolor=[0.5, 0.8, 0.5], alpha=0.75)

    plot.xlabel(x_label)
    plot.ylabel(y_label)
    plot.title(the_title)
    plot.tight_layout()
    plot.show()
