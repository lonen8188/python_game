import sys
import random
import pygame
from pygame.locals import QUIT

from sample.mine_sweeper import FPSCLOCK

# 시작하기
pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((0,0,0))

        pointlist = []

        for _ in range(10):
            xpos = random.randint(0,400)
            ypos = random.randint(0,300)
            pointlist.append((xpos,ypos))

        pygame.draw.lines(SURFACE, (255,255,255),True, pointlist,5)

        pygame.display.update()
        FPSCLOCK.tick(1)

if __name__ =='__main__':
    main()
