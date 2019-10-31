import pygame, sys, random
from pygame.locals import *

w = 800
h = 480

z = 0

screen = pygame.display.set_mode((w,h))

pygame.display.update()

class Ball:
        def __init__(self, radius, y, x, color, size, maxforce, force, life):
                self.y=y
                self.x=x
                self.size=size
                self.maxforce=maxforce
                self.force=force
                self.radius=radius
                self.color=color
                self.life=life
                pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

        def fall(self):
                if self.y < h-self.radius:
                        self.y+=self.force
                        if self.force < self.maxforce:
                                self.force+=1
                elif self.y > h-self.radius or self.y == h-self.radius:
                        self.y = h-self.radius-1
                        self.force = self.force*-1
                        self.maxforce = self.maxforce/2
                pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
                self.life-=1
                if self.life < 0:
                        ball.remove(self)


clock = pygame.time.Clock()
ball = []
ball.append(Ball(25, 250, 250, (random.randint(1,255),random.randint(1,255),random.randint(1,255)),"L", 25, 1 ,100))

while 1:
        clock.tick(60)
        x,y = pygame.mouse.get_pos()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                        z = 1
                elif event.type == MOUSEBUTTONUP:
                        z = 0

        if z == 1:
                ball.append(Ball(25, y, x, (random.randint(1,255),random.randint(1,255),random.randint(1,255)),"L", 25, 1 ,100))
                z = 3
        elif z > 1:
                z-=1

        screen.fill((0,0,0))

        for i in ball:
                i.fall()

        pygame.display.update()
