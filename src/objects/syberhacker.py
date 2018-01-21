from moveable import *
#The cyberhacker is moveable, so we can control him.
class Syberhacker(Moveable):

    #that's pretty much it really
    def __init__(self, x, y):
        super(Syberhacker, self).__init__(x, y, "assets/characters/Syberhacker1.png", "left")
