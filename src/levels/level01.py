import pygame

class level01:
    global background
    global foreground
    global colormap
    global objectdict
    #bootspawn is an optional bool, that's suposed to say if we're transitioning from another room or starting here.
    def __init__(self, bootspawn = ''):
        print("Loading level01")
        if bootspawn:
            print("loaded level with bootspawn flag set")
        self.background = pygame.image.load("assets/levels/level01/screen1.png")
        self.foreground = pygame.image.load("assets/levels/level01/foreground.png")
        self.colormap = pygame.image.load("assets/levels/level01/colormap.png")
        #this dict tells us where to place objects
        self.objectdict = {}
        self.objectdict[(0, 0, 255, 255)] = "player"
        self.objectdict[(255, 255, 0, 255)] = "froggo"

