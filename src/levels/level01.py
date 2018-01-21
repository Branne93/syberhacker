import pygame

class level01:
    global background
    global foreground
    global colormap
    def __init__(self):
        print("Loading level01")
        self.background = pygame.image.load("assets/levels/level01/screen1.png")
        self.foreground = pygame.image.load("assets/levels/level01/foreground.png")
        self.colormap = pygame.image.load("assets/levels/level01/colormap.png")
