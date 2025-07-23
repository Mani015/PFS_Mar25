
import numpy as np

# print(help(np.arange))

# arange([start,] stop[, step,], dtype=None, *, like=None)
#
#     Return evenly spaced values within a given interval.
#
#     ``arange`` can be called with a varying number of positional arguments:
#
#     * ``arange(stop)``: Values are generated within the half-open interval
#       ``[0, stop)`` (in other words, the interval including `start` but
#       excluding `stop`).


# a1 = np.arange(1,50,0.75)
# print(a1)



l1 = np.linspace(10,20,3,endpoint=True,retstep=True)
print(l1)