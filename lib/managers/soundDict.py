import os
from pygame import mixer

class soundDict:
    def __init__(self, location : str = None) -> None:
        self.__sound_dict__ = {}
        if location:
            self.load_sounds(location)
    
    def load_sound(self, location):
        key = os.path.split(location)[1][:-4]
        if key:
            self.__sound_dict__[key] = mixer.Sound(location)
        return self.__sound_dict__[key]
    
    def load_sounds(self, directory : str = "resources/sounds/"):
        for filename in os.listdir(directory):
            if filename.endswith('.wav'):
                path = os.path.join(directory,filename)
                key = filename[:-4]
                self.__sound_dict__[key] = mixer.Sound(path)
    
    def get_sound(self, name : str, notFound = None):
        return self.__sound_dict__.get(name, notFound)
    