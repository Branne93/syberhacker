import pygame

class level01:
    global background
    global foreground
    global colormap
    global objectdict
    def __init__(self):
        print("Loading level01")
        self.background = pygame.image.load("assets/levels/level01/screen1.png")
        self.foreground = pygame.image.load("assets/levels/level01/foreground.png")
        self.colormap = pygame.image.load("assets/levels/level01/colormap.png")
        self.objectdict = {}
        self.objectdict[(0, 0, 255, 255)] = "player"
        self.objectdict[(255, 255, 0, 255)] = "froggo"

