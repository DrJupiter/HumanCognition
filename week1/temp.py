import pygame
from pygame.constants import QUIT, RESIZABLE, VIDEORESIZE
import numpy as np
import os

white = (235, 255, 255)
black = (0, 0, 0)
red = (255,0,0)
blue = (0,0,255)
yellow = (255, 255, 0)
brown = (100,42,42)
pygame.display.set_caption("Missionaries and Cannibals Problem")

width = 500
height = 500

pygame.display.init()
screen = pygame.display.set_mode((width, height),RESIZABLE)
clock = pygame.time.Clock()

# initial display -> generate_scene(state, boat)
screen.fill((255, 255, 255))
pygame.draw.line(screen,blue,(int(width*3/10),height),(int(width*7/10),0),int(width*4/10))
#pygame.draw.circle(screen,red,(50,100),10,9)
pygame.display.update()

def draw_miss(x,y):
    pygame.draw.circle(screen,black,(x,y),10)

def draw_cann(x,y):
    pygame.draw.circle(screen,red,(x,y),10)
    #pygame.draw.polygon(screen,red,[[x,y],[x+2,y+1],[x,y+2]],4)

state = np.array([2,2,1])
boat = np.array([1,1,1])

def draw_state(state, boat):
    
    # in boat stuff
    if state[2] == 1:
        lstate = state - boat + np.array([0,0,1])
        rstate = state
    else:
        rstate = state + boat - np.array([0, 0, 1])
        lstate = state

    # missionaries
    for i in range(lstate[0]):
        draw_miss(150-22*i,200)
    
    for i in range(3-rstate[0]):
        draw_miss(395+22*i,200)
    

    # canibals
    for i in range(lstate[1]):
        draw_cann(140-22*i,225)

    for i in range(3-rstate[1]):
        draw_cann(385+22*i,225)

##################

    # boat
    if state[2] == 1:

        pygame.draw.line(screen,brown,(180, 212),(230, 212), 8)
        for i in range(boat[0]):
            draw_miss(194+22*i,205)
        for i in range(boat[1]):
            draw_cann(194+22-22*i, 205)

    else:
        pygame.draw.line(screen,brown,(300,212),(350,212),6)
        for i in range(boat[0]):
            draw_miss(314+22*i,205)
        for i in range(boat[1]):
            draw_cann(314+22-22*i, 205)



draw_state(state,boat)


pygame.display.update()
while True:
    pygame.event.pump()
    event = pygame.event.wait()

    if event.type == QUIT:
        break

    elif event.type == VIDEORESIZE:
        # resize
        # get width and height
        screen.fill((255, 255, 255))
        pygame.draw.line(screen,blue,(int(width*3/10),height),(int(width*7/10),0),int(width*3/10))
        draw_state(state, boat)
        pygame.display.update()



