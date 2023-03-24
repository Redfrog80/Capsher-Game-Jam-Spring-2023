import numpy as np


class Base:
    """Base class for all game object"""

    def __init__(self, name: str = "", coo: tuple = (0, 0), vel: tuple = (0, 0), acc: tuple = (0, 0)) -> None:
        self.name = name
        self.coordinate = np.array(coo, dtype=np.float)
        self.velocity = np.array(vel, dtype=np.float)
        self.acceleration = np.array(acc, dtype=np.float)
