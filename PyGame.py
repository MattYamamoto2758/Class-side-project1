import pygame
import sys
import random
from pygame import*
pygame.init()


def game():

    width, height = 1200, 600
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption('Pong')
    background = pygame.image.load('rainbow.wallpaper.jpg')
    background = pygame.transform.scale(background, (width,height))
    screen.blit(background, (0,0))

    # player item
    paddle = pygame.image.load('paddle.png')
    paddle = pygame.transform.scale(paddle, (20,200))
    px,py = 100, 200
    screen.blit(paddle, (px,py))

    # player item
    px1,py1 = 1100, 200
    width1, height1 = 20, 200
    paddle2 = pygame.image.load('paddle2.png')
    paddle2 = pygame.transform.scale(paddle2,(width1, height1))
    screen.blit(paddle2, (px1,py1))

    
    # ball
    target = pygame.image.load('target.png')
    target = pygame.transform.scale(target, (35,35))
    targetplace = target.get_rect()
    screen.blit(target, targetplace)

    movex = movey = 0
    movex1 =movey1 = 0 
    speed = [6,2]
    
    while True:
        targetplace.move_ip(speed)
        screen.blit(background,(0,0))
        screen.blit(target,targetplace)
        screen.blit(paddle,(px,py))
        screen.blit(paddle2,(px1,py1))
        pygame.display.update()

        #Key board movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    movey = -4

                if event.key == K_DOWN:
                    movey = 4

                if event.key == K_w:
                    movey1 = -4

                if event.key == K_s:
                    movey1 = 4

            elif event.type == KEYUP:
                if event.key == K_UP:
                    movey = 0

                if event.key == K_DOWN:
                    movey = 0

                if event.key == K_w:
                    movey1 = 0

                if event.key == K_s:
                    movey1 = 0
                    
        py1 = py1 + movey
        py = py + movey1    
        if targetplace[0] > width or targetplace[0]< 0:
            speed[0] = -speed[0]
         
        if targetplace[1] > height or targetplace[1]< 0:
            speed[1] = -speed[1]

        if pygame.sprite.collide_rect(target,paddle2):
            speed[0] *= -1

if __name__ == '__main__':
    game()
        
