from gameobject import *

#froggo inherits gameobject, since he cannot move
class Froggo(Gameobject):
    #the frgggo has dialogue
    global dialogue
    global speechcolor
    def __init__(self, x, y):
        super(Froggo, self).__init__(x, y, "assets/characters/Groda1.png")
        self.dialogue = []
        #This shows that the froggo is able to be spoken to
        self.interactstring = "talk"
        self.speechcolor = (0, 255, 0)
        #this is the dialogue, made of tuples containging who speaks and what they say
        self.dialogue.append(("player", "What a big froggo"))
        self.dialogue.append(("froggo", "I am the guardian"))
        self.dialogue.append(("froggo", "Prostrate yourself"))
        self.dialogue.append(("player", "I wish to have access"))
        self.dialogue.append(("froggo", "You are not allowed"))
        self.dialogue.append(("froggo", "in the beyond"))
        self.dialogue.append(("player", "It is critical"))
        self.dialogue.append(("player", "that I reach"))
        self.dialogue.append(("player", "the beyond"))
        
