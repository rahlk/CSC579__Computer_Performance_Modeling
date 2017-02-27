from __future__ import division
from __future__ import print_function
import numpy as np
import matplotlib.style
import matplotlib.mlab as mlab
import matplotlib.pyplot as plot
from pdb import set_trace

GRY_538 = "#666666ff"
RED_538 = "#ff5e53ff"
BLU_538 = "#4eb8ffff"

def line(x, y, axis="auto", x_label="X", y_label="Y", the_title="Title", x_min=0, x_max=1, y_min=0, y_max=1):
    """
    Plot a histogram of the data
    """

    plot.style.use('fivethirtyeight')
    plot.rcParams["font.family"] = "monospace"

    plot.plot(x, y, linewidth=2)

    plot.xlabel(x_label)
    plot.ylabel(y_label)
    plot.title(the_title)
    if not axis == "auto":
        plot.axis([x_min, x_max, y_min, y_max])
    plot.show()

def line2(x, y, x_1, y_1, label_1="label_1", label_2="label_2", x_label="X", y_label="Y", the_title="Title"):
    """
    Plot a histogram of the data
    """

    plot.style.use('fivethirtyeight')
    plot.rcParams["font.family"] = "monospace"

    line_1, = plot.plot(x, y, RED_538, linewidth=2, label=label_1)
    line_2, = plot.plot(x_1, y_1, GRY_538, linewidth=2, label=label_2)

    plot.legend(loc=7)

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
