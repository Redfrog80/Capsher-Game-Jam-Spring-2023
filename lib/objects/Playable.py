from .GameObject import GameObject


class Playable(GameObject):
    """Generic class for both player and enemy"""
    def __init__(self, name: str = "", pos: tuple = (0, 0), size: tuple = (0, 0),
                 img: str = "resources/images/notfound.png"):
        super().__init__(name, pos, size, img)

        # stat
        self.health = 0
        self.shield = 0
        self.accMag = 0;

        weapon = {}

    
