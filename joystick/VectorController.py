import pygame, sys, random
from pygame.locals import *

sys.path.insert(1, 'D:/Misc/VectorAPI/API Files')

from VectorAPIBeginner import *
from JoystickClass import *

vector = VectorOBJ("00403e6f")
vector.connect()

w = 400
h = 400

screen = pygame.display.set_mode((w,h))

pygame.display.update()

clock = pygame.time.Clock()
joystick = Joystick()

while 1:
        clock.tick(60)
        x,y = pygame.mouse.get_pos()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        sys.exit()


        screen.fill((255,255,255))

        if joystick.getX() > 180 and joystick.getY() < 200 and joystick.getY() > 150:
            print("going right")
            vector._VectorOBJ__set_wheel_motors(-50, 50)

        if joystick.getX() < 175 and joystick.getY() < 200 and joystick.getY() > 150:
            print("going left")
            vector._VectorOBJ__set_wheel_motors(50, -50)

        if joystick.getY() > 180 and joystick.getX() > 150 and joystick.getX() < 200:
            print("going down")
            vector._VectorOBJ__set_wheel_motors(-50, -50)

        if joystick.getY() < 175 and joystick.getX() > 150 and joystick.getX() < 200:
            print("going up")
            vector._VectorOBJ__set_wheel_motors(50, 50)

        else:
            vector._VectorOBJ__stop_wheel_motors

        joystick.draw(screen)
        joystick.update()

        pygame.display.update()
