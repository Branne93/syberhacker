from syberhacker import *
from froggo import *

class Gameobjectfactory:

    def __init__(self):
        pass

    def create_object(self, name, x, y):
        if name == "player":
            return Syberhacker(x, y)
        elif name == "froggo":
            return Froggo(x, y)
