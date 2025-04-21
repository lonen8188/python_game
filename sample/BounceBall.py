import pygame
from pygame.locals import *
import sys
import random
from Ball import *             # Ball 클래스 import
import time


BLACK = (0, 0, 0)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30 
       
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  

# 1.Ball 클래스 활용하여 oBall 객체 생성 -> 2. 리스트로 생성
prevTime = time.time()

oBalls = []

'''for oBall in range(5):
   oBall = Ball(window,WINDOW_WIDTH,WINDOW_HEIGHT)
   oBalls.append(oBall)'''

#oBall = Ball(window,WINDOW_WIDTH,WINDOW_HEIGHT)
#oBall2 = Ball(window,WINDOW_WIDTH,WINDOW_HEIGHT)


while True:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()          

    #3. 1초마다 볼 생성하기 (10개 제한)
    if time.time() - prevTime >= 1 and len(oBalls)<10:
        oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
        oBalls.append(oBall)
        prevTime = time.time()

    # 공 상태 갱신
    for oBall in oBalls:
        oBall.update()
 #   oBall.update()
 #   oBall2.update()

    window.fill(BLACK)
    
    # 공을 윈도우에 그린다.
    for oBall in oBalls:
        oBall.draw()
 #   oBall.draw()
 #   oBall2.draw()

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)  
