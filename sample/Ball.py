import pygame
from pygame.locals import *
import random

# Ball class 
class Ball():

    def __init__(self, window, windowWidth, windowHeight):
        self.window = window  # 나중에 그릴 수 있도록 윈도우 기억
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        imglist = ['images/balloon1-a.png','images/balloon1-b.png','images/balloon1-c.png']
        self.image = pygame.image.load(imglist[random.randint(0,len(imglist)-1)]  )
        ballRect = self.image.get_rect()
        self.width = ballRect.width + random.randint(-50, 50)
        self.height = ballRect.height  + random.randint(-50, 50)
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height
        
        self.x = random.randrange(0, self.maxWidth)
        self.y = random.randrange(0, self.maxHeight)

        speedsList = [-4, -3, -2, -1, 1, 2, 3, 4] 
        self.xSpeed = random.choice(speedsList)
        self.ySpeed = random.choice(speedsList)

    def update(self):
        # 벽에 닿았는지 체크 후 방향 전환 
        if (self.x < 0) or (self.x >= self.maxWidth):
            self.xSpeed = -self.xSpeed

        if (self.y < 0) or (self.y >= self.maxHeight):
            self.ySpeed = -self.ySpeed

        # Update the Ball's x and y, using the speed in two directions
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))
