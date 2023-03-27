import pygame
import numpy as np

from lib.objects.gameObject import gameObject

from ..imageDict import imageDict
from .gameObject import gameObject

class staticCamera(gameObject):
    def __init__(self, position: np.array = np.array([0,0])):
        super().__init__(position, None, None)
