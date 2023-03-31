# utility function
from math import *


def addTuple(a, b):
    return a[0] + b[0], a[1] + b[1]


def subTuple(a, b):
    return a[0] - b[0], a[1] - b[1]


def mulTuple(a: tuple, b: float):
    return a[0] * b, a[1] * b


def divTuple(a: tuple, b: float):
    return a[0] / b, a[1] / b


def floorElementDiv(a: tuple, b: tuple):
    return a[0] // b[0], a[1] // b[1]


def magnitude(a: tuple):
    return sqrt(a[0]**2 + a[1]**2)


def capRange(a, lo, hi):
    if a < lo:
        return lo
    elif a > hi:
        return hi
    else:
        return a
