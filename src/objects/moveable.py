from gameobject import *

class Moveable(Gameobject):
    global direction
    
    def __init__(self, x, y, imagepath, direction):
        super(Moveable, self).__init__(x, y, imagepath)
        self.direction = direction

    #move up or down
    def shifty(self, amount):
        self.y += amount
        self.updaterectangles()

    #moving objects should be able to face left and right
    def shiftx(self, amount):
        if amount > 0 and not self.direction == "right":
            self.direction = "right"
            self.image = pygame.transform.flip(self.image, True, False)
        elif amount < 0 and not self.direction == "left":
            self.direction = "left"
            self.image = pygame.transform.flip(self.image, True, False)
        
        self.x += amount
        self.updaterectangles()

    #updates the rectangles around the objects
    def updaterectangles(self):
        self.rect = pygame.Rect(self.x, self.y + self.image.get_height(), self.image.get_width(),  self.image.get_height())
        self.floorrect = pygame.Rect(self.x, self.y + self.image.get_height(), self.image.get_width(),  self.image.get_height() - self.image.get_height() * 0.9)

