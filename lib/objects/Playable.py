from .GameObject import GameObject


class Playable(GameObject):
    """Generic class for both player and enemy"""
    def __init__(self, name: str = "", pos: tuple = (0, 0), size: tuple = (0, 0),
                 img: str = "resources/images/notfound.png"):
        super().__init__(name, pos, size, img)

        # stat
        health = 0
        shield = 0
        speed = 0

        weapon = {}

    
