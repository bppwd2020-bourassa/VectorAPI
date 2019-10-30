import pygame
from pygame.locals import *

pygame.init()
screenwidth = 400
screenheight =400
win=pygame.display.set_mode((screenwidth,screenheight))

clock = pygame.time.Clock()

global x
global y

x = 175
y = 175
width = 50
height = 50

def draw():
	pygame.draw.rect(win,(255,255,255),pygame.Rect(0,0,screenwidth,screenheight))
	pygame.draw.rect(win,(255,0,0),pygame.Rect(x,y,width,height))

def update():
    global x
    global y
    pygame.display.update()
    clickX = pygame.mouse.get_pos()[0]
    clickY = pygame.mouse.get_pos()[1]
    if pygame.mouse.get_pressed()[0] == 1:
        if clickX >= x and clickX <= x + width and clickY >= y and clickY <= y + height:
            x = clickX
            y = clickY

        else:
            print(clickX, clickY)

run = True
while run:

	clock.tick(60)
	pressed = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT or pressed[pygame.K_ESCAPE]:
			run = False

	draw()
	update()


pygame.quit()
