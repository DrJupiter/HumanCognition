import pygame
from pygame.constants import QUIT, RESIZABLE, VIDEORESIZE
import numpy as np

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255, 255, 0)
BROWN = (100,42,42)

def draw_miss(x,y, screen):
    pygame.draw.circle(screen,BLACK,(x,y),10)

def draw_cann(x,y, screen):
    pygame.draw.circle(screen,RED,(x,y),10)
    #pygame.draw.polygon(screen,red,[[x,y],[x+2,y+1],[x,y+2]],4)


def draw_state(state, boat, screen):
    
    # in boat stuff
    if state[2] == 1:
        lstate = state - boat + np.array([0,0,1])
        rstate = state
    else:
        rstate = state + boat - np.array([0, 0, 1])
        lstate = state

    # missionaries
    for i in range(lstate[0]):
        draw_miss(150-22*i,200, screen)
    
    for i in range(3-rstate[0]):
        draw_miss(395+22*i,200, screen)
    

    # canibals
    for i in range(lstate[1]):
        draw_cann(140-22*i,225, screen)

    for i in range(3-rstate[1]):
        draw_cann(385+22*i,225, screen)

##################

    # boat
    if state[2] == 1:

        pygame.draw.line(screen,BROWN,(180, 212),(230, 212), 8)
        for i in range(boat[0]):
            draw_miss(194+22*i,205, screen)
        for i in range(boat[1]):
            draw_cann(194+22-22*i, 205, screen)

    else:
        pygame.draw.line(screen,BROWN,(300,212),(350,212),6)
        for i in range(boat[0]):
            draw_miss(314+22*i,205, screen)
        for i in range(boat[1]):
            draw_cann(314+22-22*i, 205, screen)


def render_help_txt(screen, txt_config):
    ppl_info_txt = [
        txt_config.render("= Missionary", False, BLACK),
        txt_config.render("= Cannibal", False, BLACK)
    ]
    
    move_info_txt = [
        txt_config.render("m -> Move missionary INTO boat", False, BLACK),
        txt_config.render("M -> Move missionary FROM boat", False, BLACK),
        txt_config.render(" ", False, BLACK),
        txt_config.render("c -> Move cannibal INTO boat", False, BLACK),
        txt_config.render("C -> Move cannibal FROM boat", False, BLACK),
        txt_config.render(" ", False, BLACK),
        txt_config.render("b or B -> Move boat to the other side and unload", False, BLACK),
        txt_config.render("q or Q -> Quit", False, BLACK)
    ]

    for i in range(len(move_info_txt)):
        screen.blit(move_info_txt[i],(10,330+i*20))

    for i in range(len(ppl_info_txt)):
        screen.blit(ppl_info_txt[i],(50,12+i*35))

    draw_miss(30,30, screen)
    draw_cann(30,60, screen)

def render_err_txt(screen, err, txt_config):
    error_txt = txt_config.render(err, False, BLACK)
    screen.blit(error_txt, (200,20))

def generate_scene(state, boat, screen, width, height, txt_config, err=""):
    screen.fill(WHITE)
    pygame.draw.line(screen,BLUE,(int(width*3/10),height),(int(width*7/10),0),int(width*4/10))
    pygame.draw.line(screen, WHITE,(0,0),(width,0),int(height*2/4))
    pygame.draw.line(screen, WHITE,(0,height),(width,height),int(height*3/4))

    draw_state(state, boat, screen)

    render_err_txt(screen, err, txt_config)
    render_help_txt(screen, txt_config)
    
    pygame.display.update()


if __name__ == "__main__":


    pygame.display.set_caption("Missionaries and Cannibals Problem")
    
    width = 500
    height = 500
    
    pygame.display.init()
    screen = pygame.display.set_mode((width, height),RESIZABLE)
    clock = pygame.time.Clock()
    
    # initial display -> generate_scene(state, boat)
    screen.fill((255, 255, 255))
    pygame.draw.line(screen,BLUE,(int(width*3/10),height),(int(width*7/10),0),int(width*4/10))
    pygame.draw.line(screen,White,(0,0),(width,0),int(height*2/4))
    pygame.draw.line(screen,White,(0,height),(width,height),int(height*3/4))
    #pygame.draw.circle(screen,red,(50,100),10,9)
    pygame.display.update()
    state = np.array([2,2,1])
    boat = np.array([1,1,1])

    draw_state(state,boat, screen)
    
    
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
            pygame.draw.line(screen,BLUE,(int(width*3/10),height),(int(width*7/10),0),int(width*4/10))
            pygame.draw.line(screen,White,(0,0),(width,0),int(height*2/4))
            pygame.draw.line(screen,White,(0,height),(width,height),int(height*3/4))
            draw_state(state, boat, screen)
            pygame.display.update()

