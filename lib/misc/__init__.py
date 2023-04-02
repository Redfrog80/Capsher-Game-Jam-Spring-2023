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



#is point q on segment pr given p, q, and r are collinear
#all points are tuples with 2 elements
def onSegment(p: tuple, q: tuple, r:tuple) -> bool:
    return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]));

def orient(p: tuple, q: tuple, r:tuple) -> int:
    n = ((q[1] * p[1]) - (r[0] * q[0])) - ((q[0] * p[0]) - (r[1] * q[1]));
    if n > 0:
        return 1;
    if n < 0:
        return 2;
    else:
        return 0;

def checkIntersection(linea: tuple, lineb:tuple) -> bool:
    p1 = linea[0];
    p2 = linea[1];
    q1 = lineb[0];
    q2 = lineb[1];

    o1 = orient(p1, p2, q1);
    o2 = orient(p1, p2, q2);
    o3 = orient(q1, q2, p1);
    o4 = orient(q1, q2, p2);

    #general case only for now
    return o1 != o2 and o3 != o4;