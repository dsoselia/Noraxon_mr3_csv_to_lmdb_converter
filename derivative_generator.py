#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 12:02:08 2018

@author: davitisoselia
"""

import numpy as np
import matplotlib.pyplot as plt

#
def nth_derivative (N, order = 1):
    res = [N]
    for i in range(order):
        res.append(derivative(res[-1])) 
    return np.array(res[-1])
    
def derivative(n):
    if type(n) is not np.ndarray: 
        n = np.array(n)
    return np.gradient(n)[1]

def gradient(y, dx=1):
    """Returns second order accurate derivative of y using constant step size dx."""

    assert np.isscalar(dx), "dx must be a constant."

    dy = np.zeros_like(y)

    # Second order forward difference for first element
    dy[0] = -(3*y[0] - 4*y[1] + y[2]) / (2*dx)

    # Central difference interior elements
    dy[1:-1] = (y[2:] - y[0:-2])/(2*dx)

    # Backwards difference final element
    dy[-1] = (3*y[-1] - 4*y[-2] + y[-3]) / (2*dx)

    return dy

def test_derivative():
    f = np.arange(0.0, 100,0.01)
    f = np.power(f,3)
    f2 = np.power(f,4)
    J = np.array([f,f2])
    Y = nth_derivative(J,2)
    plt.plot(Y[1])
    plt.show()
    plt.plot(Y[0])
    plt.show()
