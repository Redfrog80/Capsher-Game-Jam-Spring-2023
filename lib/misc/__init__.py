# utility function
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