import pygame
from objects.moveable import *

class Controller:
    global model
    global view
    global done
    global dt
    global movespeed
    global collided_gameobject

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
        self.collided_gameobject = self.model.player_collide()
        self.draw_scene()
        self.read_input()
        self.view.flip()
        self.collided_gameobject = None

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
        #this should probably be abstracted so thjat each object knows how it's to be interacted with, much cleaner
        if self.collided_gameobject:
            if(self.collided_gameobject.interactstring== "talk"):
                self.view.drawstring("press space to talk", self.model.player.x, self.model.player.y-10, (255, 255, 255))
            else:
                self.view.drawstring("interact", self.model.player.x, self.model.player.y-10, (255, 255, 255))



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
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE and self.collided_gameobject:
                    self.interact(self.model.player, self.collided_gameobject)

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



    def interact(self, player, gameobject):
        if(self.collided_gameobject.interactstring== "talk"):
            self.start_conversation(player, gameobject)
        else:
            print("unhandled interaction type!")

    def start_conversation(self, player, gameobject):
        self.collided_gameobject = None
        for stringtuple in gameobject.dialogue:
            print(stringtuple)
            if(stringtuple[0] == "player"):
                #draw over the earlier prompt
                self.draw_scene()
                self.view.drawstring(stringtuple[1], player.x, player.y-10, player.speechcolor)
            else:
                self.draw_scene()
                self.view.drawstring(stringtuple[1], gameobject.x, gameobject.y-10, gameobject.speechcolor)
            #update the screen to view the conversation
            self.view.flip()
            spacenotpressed = True
            while spacenotpressed:
                for event in pygame.event.get():
                    spacenotpressed = not (event.type == pygame.KEYUP and event.key == pygame.K_SPACE)
                    
