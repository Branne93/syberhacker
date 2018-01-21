import pygame
from objects.moveable import *

class Controller:
    global model
    global view
    global done
    global dt
    global movespeed
    global interactstring

    #Basic constructor for basicly everything, nothing fancy.
    def __init__(self, model, view):
        init = "initializing controller"
        print(init)
        self.model = model
        self.view = view
        self.done = False
        self.interactstring = None
        self.movespeed = 50
        init = "controller has been initialized"
        print(init)

    #main update method, dt is delta time which is time since last update. Compensates for different hardware.
    def update(self, dt):
        self.dt = dt
        self.interactstring = self.model.player_collide()
        self.draw_scene()
        self.read_input()
        self.view.flip()

    #draw the loaded level and all the game objects.
    def draw_scene(self):
        #background should be in the back
        self.view.draw(self.model.level.background, (0,0))

        #Sort game objects on y position to make them appear in correct order,
        objectlist = sorted(self.model.objectlist, key=lambda gameobject: gameobject.y)
        
        for gameobject in objectlist:

            #these are some rectangles that can eb drawn to see collisions
            #self.view.drawrect(gameobject.rect, (255, 255, 0))
            #self.view.drawrect(gameobject.floorrect, (255, 0, 0))
            self.view.draw(gameobject.image, (gameobject.x, gameobject.y))
        #foreground should be in the fore
        self.view.draw(self.model.level.foreground, (0,0))

        #if we can interact, we want a string to prompt us
        if self.interactstring:
            self.view.drawstring(self.interactstring, self.model.player.x, self.model.player.y-10)


    #move the moveable characters.
    def control_char(self, direction, amount):
        for gameobject in self.model.objectlist:
            if isinstance(gameobject, Moveable):
                self.model.move_object(direction, amount, gameobject)


    #read the input and react to the given events.
    def read_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.done = True

        keys = pygame.key.get_pressed()

        #what keys were pressed?
        if keys[pygame.K_UP]:
            self.control_char("up", self.movespeed*self.dt)
        if keys[pygame.K_DOWN]:
            self.control_char("down", self.movespeed*self.dt)
        if keys[pygame.K_LEFT]:
            self.control_char("left", self.movespeed*self.dt)
        if keys[pygame.K_RIGHT]:
            self.control_char("right", self.movespeed*self.dt)

