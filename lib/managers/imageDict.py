import os
from pygame import image

class imageDict:
    def __init__(self, location : str = None) -> None:
        self.__image_dict__ = {}
        if location:
            self.load_images(location)
    
    def load_image(self, location  : str = "resources/images/notfound.png"):
        key = os.path.split(location)[1][:-4]
        if key:
            self.__image_dict__[key] = image.load(location).convert_alpha()
        return self.__image_dict__[key]
    
    def load_images(self, directory : str = "resources/images/"):
        for filename in os.listdir(directory):
            if filename.endswith('.png'):
                path = os.path.join(directory,filename)
                key = filename[:-4]
                self.__image_dict__[key] = image.load(path).convert_alpha()
    
    def get_image(self, name : str, notFound = None):
        return self.__image_dict__.get(name, notFound)
    
    def get_image_dimensions(self, name : str, notFound = None):
        image = self.__image_dict__.get(name, None)
        if image != None:
            return (image.get_width(), image.get_height())
        else:
            return notFound