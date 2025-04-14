#!/bin/python3
import numpy as np
from scipy.integrate import quad

def integrate(f, a, b):
    resultado, error = quad(f, a, b)
    print(f"Integral ~ {resultado} con error: {error}")

integrate(lambda x : x**3 * np.exp(-x**3), -1, np.inf)