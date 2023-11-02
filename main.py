import numpy as np
import pandas as pd

import os
import sys

m = 1
k = 1


def f(q, p):
    # f(x) is the derivative for (q, p) with repect to time
    dq_dt = 1 / m * p
    dp_dt = -k * q

    return dq_dt, dp_dt


# Forward Euler
def forwardEuler(num, t_arr, q_arr, p_arr):
    for i in range(len(num)):
        q_arr, p_arr


if __name__ == "__main__":
    num = 10
    t_arr = np.linspace(1, num, num)
    q_arr = np.empty(num)
    p_arr = np.empty(num)
