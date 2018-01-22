import pygame

class Gameobject(object):
    global x
    global y
    global image
    global rect
    global floorrect
    global interactstring
    
    #This is a basic class for an abstract game object. All objects in the game have a position, an image
    #and two rectangles, a basic image rectangle and a floor rectangle.
    def __init__(self, x, y, imagepath):
        self.x = x
        self.y = y
        self.image = pygame.image.load(imagepath)
        self.rect = pygame.Rect(x, y, self.image.get_width(),  self.image.get_height())
        self.floorrect = pygame.Rect(x, y, self.image.get_width(),  self.image.get_height() - self.image.get_height() * 0.9)
        #this is the string that decides if and how the player interacts with the object. Default an object isn't interactable.
        self.interactstring = None
