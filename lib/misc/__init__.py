# utility function
from math import *


def addTuple(a, b):
    return a[0] + b[0], a[1] + b[1]


def subTuple(a, b):
    return a[0] - b[0], a[1] - b[1]


def mulTuple(a: tuple, b: float):
    return (a[0] * b, a[1] * b)

def mulElements(a: tuple, b: tuple):
    return a[0] * b[0], a[1] * b[1]

def divTuple(a: tuple, b: float):
    return a[0] / b, a[1] / b

def floorElementDiv(a: tuple, b: tuple):
    return (a[0] // b[0], a[1] // b[1])

def elementDiv(a: tuple, b: float):
    return (a[0] / b[0], a[1] / b[1])

def elementInverse(a: tuple):
    return (1 / a[0], 1 / a[1])

def absTuple(a: tuple):
    return (abs(a[0]), abs(a[1]))

def dotTuple(a: tuple, b: tuple):
    return a[0] * b[0] + a[1] * b[1]

def unitTuple(origin: tuple, a: tuple):
    diff = subTuple(origin,a)
    if (False in [i==0 for i in diff]):
        mag = magnitude(a)
        if (mag):
            return divTuple(diff,mag)
    return (0,0)

def magnitude(a: tuple):
    return sqrt(a[0]**2 + a[1]**2)

def capRange(a, lo, hi):
    if a < lo:
        return lo
    elif a > hi:
        return hi
    else:
        return a
