from .GameObject import GameObject;

class Gun(GameObject):
    def __init__(self, name: str = "", pos: tuple = ..., size: tuple = ..., img: str = "resources/images/notfound.png"):
        super().__init__(name, pos, size, img);

    def shoot():
        pass;
        #shoot boolet