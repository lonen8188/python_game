# 1 - 패키지 불러오기
import pygame
from pygame.locals import *
import sys
import math

# 2 - 상수 정의하기
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 5

# 3 - 파이게임 환경 초기화하기
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 
# 4 - 이미지, 소리 등 애셋 불러오기
ballimage = pygame.image.load("images/ball.png")
# 5 - 변수 초기화하기
ballX = 150
ballY = 0

# 6 - 무한루프 수행하기
while True:

    # 7 - 이벤트 발생 검사 및 처리하기
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()

    # 8 - ‘프레임당’ 처리해야 할 일 정의하기
    # 각도를 움직일 때 cos(), sin()으로 이용가능함
#    ballX = ballX + math.cos(math.radians(30)) * 50
#    ballY = ballY + math.sin(math.radians(30)) * 50
    if ballY <= WINDOW_HEIGHT:
        ballY = ballY + 10
    else:
        ballY = 0

    # 9 - 윈도우 내 내용물(요소) 지우기
    window.fill(BLACK)
    
    # 10 - 윈도우 내 모든 요소 그리기
    window.blit(ballimage, (ballX, ballY))
    # 11 - 윈도우 갱신하기 : 윈도우에 포함될 모든 요소를 실제 윈도우에 출력
    pygame.display.update()

    # 12 - 윈도우 갱신 주기 늦추기
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
