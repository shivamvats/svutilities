import numpy as np


def getRandInRange(a, b, shape=None):
    """Get a random float or float array within some range."""
    if shape is None:
        return a + (b - a) * np.random.rand()
    else:

        return a + (b - a) * np.random.rand(*shape)

