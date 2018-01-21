from gameobject import *

#froggo inherits gameobject, since he cannot move
class Froggo(Gameobject):
    global dialogue
    global interactstring
    def __init__(self, x, y):
        super(Froggo, self).__init__(x, y, "assets/characters/Groda1.png")
        self.dialogue = []
        self.interactstring = "press space to talk"
        #this is the dialogue, made of tuples containging who speaks and what they say
        self.dialogue.append(("player", "What a big froggo"))
        self.dialogue.append(("froggo", "I am the guardian froggo, prostrate yourself"))
        self.dialogue.append(("player", "I wish to have access to the beyond"))
        self.dialogue.append(("froggo", "You are not allowed in the beyond"))
        self.dialogue.append(("player", "It is critical that I reach the beyond"))
        
