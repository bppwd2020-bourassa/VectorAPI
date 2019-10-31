import pygame, sys, random
from pygame.locals import *

w = 400
h = 400

screen = pygame.display.set_mode((w,h))

pygame.display.update()

class Joystick:

    def __init__(self):
            self.y=175
            self.x=175
            self.height = 50
            self.width = 50

    def draw(self):
    	pygame.draw.rect(screen,(0,0,0),pygame.Rect(self.x,self.y,self.width,self.height))

    def update(self):
        global x,y
        pygame.display.update()
        self.clickX = pygame.mouse.get_pos()[0]
        self.clickY = pygame.mouse.get_pos()[1]
        if pygame.mouse.get_pressed()[0] == 1:
            if self.clickX >= self.x and self.clickX <= self.x + self.width and self.clickY >= self.y and self.clickY <= self.y + self.height:
                self.x = self.clickX - 25
                self.y = self.clickY - 25
            else:
                print(self.clickX, self.clickY)
                self.x = 175
                self.y = 175
        else:
            self.x = 175
            self.y = 175

    def getX(self):
        return self.x

    def getY(self):
        return self

clock = pygame.time.Clock()
joystick = Joystick()

while 1:
        clock.tick(60)
        x,y = pygame.mouse.get_pos()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        sys.exit()


        screen.fill((255,255,255))

        joystick.draw()
        joystick.update()

        pygame.display.update()
