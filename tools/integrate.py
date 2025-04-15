#!/bin/python3
from math import sqrt
import numpy as np
from scipy.integrate import quad

def integrate(f, a, b):
    resultado, error = quad(f, a, b)
    print(f"Integral ~ {resultado} con error: {error}")

integrate(lambda x : sqrt(x + sqrt(x)), 1, 7)