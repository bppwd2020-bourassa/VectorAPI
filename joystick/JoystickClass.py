import pygame, sys, random
from pygame.locals import *


class Joystick:

    def __init__(self):
            self.y=175
            self.x=175
            self.height = 50
            self.width = 50
            self.stop = True

    def draw(self, screen):
    	pygame.draw.rect(screen,(0,0,0),pygame.Rect(self.x,self.y,self.width,self.height))

    def update(self):
        global x,y
        pygame.display.update()
        self.clickX = pygame.mouse.get_pos()[0]
        self.clickY = pygame.mouse.get_pos()[1]
        if pygame.mouse.get_pressed()[0] == 1:
            if self.clickX >= self.x and self.clickX <= self.x + self.width and self.clickY >= self.y and self.clickY <= self.y + self.height:
                self.stop = False
                self.x = self.clickX - 25
                self.y = self.clickY - 25
            else:
                print(self.clickX, self.clickY)
                self.x = 175
                self.y = 175
                self.stop = True
        else:
            self.x = 175
            self.y = 175
            self.stop = True

    def getMotion(self):
        return self.stop

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getMouseX(self):
        return self.clickX

    def getMouseY(self):
        return self.clickY
