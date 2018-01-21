from src.model import *
from src.view import *
from src.controller import *
import pygame

#set up the MVC components
pygame.init()
model = Model()
view = View()
controller = Controller(model, view)

#limit the fps to 60 and start the clock.
fps = 60
clock = pygame.time.Clock()
dt = 0
clock.tick(fps)

#main game loop, delta time is measuread at the end of the loop
while(not controller.done):
    controller.update(dt);
    dt = clock.tick(fps)/1000.0

print("Game exited")
pygame.quit()
