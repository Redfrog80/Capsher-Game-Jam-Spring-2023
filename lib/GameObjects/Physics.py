import Base
import numpy as np


class Physics(Base.Base):
    def __init__(self, name: str = "", coo: tuple = (0, 0), vel: tuple = (0, 0), acc: tuple = (0, 0),
                 bound: tuple = ((0, 0), (0, 0))) -> None:
        """
        :param name:
        :param coo:
        :param vel:
        :param acc:
        :param bound: 2 tuples: first is offset from coo. Second is width and height
        """
        super().__init__(name, coo, vel, acc)
        self.boundOffSet = np.array(bound[0], dtype=np.float)
        self.boundRange = np.array(bound[1], dtype=np.float)
