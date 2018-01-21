from objects.syberhacker import *
from objects.froggo import *
from levels.level01 import *

class Model:
    init = ""
    global level
    global objectlist
    global player

    #just a basic constructor with some prints
    def __init__(self):
        init = "initializing model"
        print(init)
        self.objectlist = []
        self.level = level01()
        self.spawnobjects()
        init = "Model has been initialized"
        print(init)
        
    #loops through the colormap, spawns the correct objects at the given position. What should be spawned should
    #not be decided here, but for now it works as testing if the idea works
    def spawnobjects(self):
        print("checking colormap for objects")
        for i in range(0, self.level.colormap.get_width()):
            for j in range(0, self.level.colormap.get_height()):
                color = self.level.colormap.get_at((i, j))
                if color[0] == 0 and color[1] == 0 and color[2] == 255 and color[3] == 255:
                    gameobject = Syberhacker(i, j)
                    gameobject.y -= gameobject.image.get_height()
                    self.player = gameobject
                    self.objectlist.append(gameobject)

                if color[0] == 255 and color[1] == 255 and color[2] == 0 and color[3] == 255:
                    gameobject = Froggo(i, j)
                    gameobject.y -= gameobject.image.get_height()
                    self.objectlist.append(gameobject)

    #Find i position x, y is not allowed
    def blockedposition(self, x, y):
        try:
            color = self.level.colormap.get_at((x, y))
        #in case we move out of bounds
        except IndexError as e:
            return True
        return color[0] == 255 and color[1] == 0 and color[2] == 0 and color[3] == 255

    #move an object, usually the player.
    def move_object(self, direction, amount, gameobject):
        #save old position
        prevx = gameobject.x
        prevy = gameobject.y
        
        #update position, this is probale poorly implemented
        if(direction == "up"):
            gameobject.shifty(-1 * amount)
        if(direction == "down"):
            gameobject.shifty(amount)
        if(direction == "left"):
            gameobject.shiftx(-1 * amount)
        if(direction == "right"):
            gameobject.shiftx(amount)

        #Is the new position illegal? if so, return to old position
        if (self.blockedposition(gameobject.floorrect.x, gameobject.floorrect.y)
            or self.blockedposition(gameobject.floorrect.x + gameobject.floorrect.w, gameobject.floorrect.y - gameobject.floorrect.h)):
            gameobject.x = prevx
            gameobject.y = prevy

    #This function handels collisions for interactions with other gameobjects.
    def player_collide(self):

        #remove the player for the list, dont want to check if we collide with ourselves.
        objectlist = self.objectlist[:]
        objectlist.remove(self.player)

        for gameobject in objectlist:
            #An interactable object has an interactstring. check if we collide with their floor rectangle
            if self.player.floorrect.colliderect(gameobject.floorrect) and gameobject.interactstring:
                return gameobject.interactstring
        #default return
        return None
