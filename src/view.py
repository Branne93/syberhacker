import pygame

class View:
    init = ""
    global screen
    global scale
    global basicfont

    #constructor for the view, setting up the game window and stuff, scale is based on the levels, since they are 200x200
    def __init__(self):
        init = "initializing view"
        print(init)
        screeninfo = pygame.display.Info()
        height = screeninfo.current_h
        self.scale = height / 200
        height = 200 * self.scale
        self.screen = pygame.display.set_mode((height, height))
        pygame.font.init()
        pygame.display.set_caption("Syberhacker")
        self.basicfont = pygame.font.SysFont(pygame.font.get_default_font(), 24)
        init = "View has been initialized"
        print(init)

    #update everything
    def flip(self):
        pygame.display.flip()

    #draw the image at position x, y and scale it properly
    def draw(self, image, (x, y)):
        image = pygame.transform.scale(image, (image.get_width()*self.scale, image.get_height()*self.scale))
        self.screen.blit(image, (x*self.scale, y*self.scale))

    #draw rectangles, also scaled properly
    def drawrect(self, rect, (r, g, b)):
        rect = pygame.Rect(rect.x * self.scale, rect.y*self.scale, rect.width*self.scale, -1 * rect.height*self.scale)
        pygame.draw.rect(self.screen, (r, g, b), rect)

     #Draws text at the given position, don't scale text, it looks horrible. scale x and y still as usual   
    def drawstring(self, string, x, y):
        self.screen.blit(self.basicfont.render(string, False, (255, 0, 255)), (x * self.scale, y * self.scale))
