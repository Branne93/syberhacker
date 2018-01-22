from moveable import *
#The cyberhacker is moveable, so we can control him.
class Syberhacker(Moveable):

    global speechcolor
    def __init__(self, x, y):
        super(Syberhacker, self).__init__(x, y, "assets/characters/Syberhacker1.png", "left")
        self.speechcolor = (255, 0, 255)
