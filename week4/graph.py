import pygame
import numpy as np
from pygame.constants import QUIT, RESIZABLE, VIDEORESIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)
BLUE = (0,0,255)

scale = 50
fatness = 4

width = 800
height = 800

pygame.font.init()
txt_config = pygame.font.SysFont('Times New Roman', 40)

#screen = pygame.display.set_mode([width,height])

def circle(x, y, color, x_resolution, y_resolution, screen):
    pygame.draw.circle(screen,color,(x,y),np.min([x_resolution,y_resolution])/scale,fatness)

def cross(x, y, color, x_resolution, y_resolution, screen):
    min_val = np.min([x_resolution,y_resolution])
    scaled_x = min_val/scale
    scaled_y = min_val/scale
    pygame.draw.line(screen,color,(x-scaled_x, y-scaled_y),(x+scaled_x, y+scaled_y),fatness)
    pygame.draw.line(screen,color,(x+scaled_x, y-scaled_y),(x-scaled_x, y+scaled_y),fatness)

def render_help_txt_info(screen, txt_config, height, width):
    intro_info_txt = [
        txt_config.render("Press \"j\" when you see a target!", False, BLACK),
        txt_config.render("Press \"f\" when you see no target", False, BLACK),
        txt_config.render("Press any key to start the experiment", False, BLACK),
    ]

    for i in range(len(intro_info_txt)):
        screen.blit(intro_info_txt[i],(width/8,height/4+i*55))

def render_help_txt_1(screen, txt_config, height, width):
    intro_info_txt = [
        txt_config.render("Welcome to visual search!", False, BLACK),
        txt_config.render("Your reaction time is measured", False, BLACK),
        txt_config.render("So be fast", False, BLACK),
        txt_config.render("But also be precise", False, BLACK),
        txt_config.render("Press any key to continue", False, BLACK)
    ]

    for i in range(len(intro_info_txt)):
        screen.blit(intro_info_txt[i],(width/8,height/4+i*55))

def render_help_txt_2(screen, txt_config, height, width):
    trail_1_info_txt = [
        txt_config.render("Target:", False, BLACK),
        txt_config.render("  X", False, BLUE),
        txt_config.render("or", False, BLACK),
        txt_config.render("  O", False, RED),
        txt_config.render(" ", False, BLACK),
        txt_config.render("Distractor:", False, BLACK),
        txt_config.render("  X", False, RED)
    ]

    for i in range(len(trail_1_info_txt)):
        screen.blit(trail_1_info_txt[i],(width/8,height/4+i*55))

def render_help_txt_3(screen, txt_config, height, width):
    trail_1_info_txt = [
        txt_config.render("Target:", False, BLACK),
        txt_config.render("X", False, BLUE),
        txt_config.render(" ", False, BLACK),
        txt_config.render("Distractors:", False, BLACK),
        txt_config.render("O", False, BLUE),
        txt_config.render("Or:", False, BLACK),
        txt_config.render("X", False, RED)
    ]

    for i in range(len(trail_1_info_txt)):
        screen.blit(trail_1_info_txt[i],(width/8,height/4+i*55))


def generate_scene(screen, width, height):
    screen.fill(WHITE)

    render_help_txt_3(screen, txt_config, height, width)

    circle(50, 50, BLUE, height, width, screen)
    cross(50, 100, BLUE, height, width, screen)

    circle(100, 50, RED, height, width, screen)
    cross(100, 100, RED, height, width, screen)
    
    pygame.display.update()






pygame.display.set_caption("Missionaries and Cannibals Problem")

pygame.display.init()
screen = pygame.display.set_mode((width, height),RESIZABLE)
clock = pygame.time.Clock()

# initial display -> generate_scene(state, boat)
screen.fill((255, 255, 255))
pygame.draw.line(screen,BLUE,(int(width*3/10),height),(int(width*7/10),0),int(width*4/10))
pygame.draw.line(screen,WHITE,(0,0),(width,0),int(height*2/4))
pygame.draw.line(screen,WHITE,(0,height),(width,height),int(height*3/4))

generate_scene(screen, width, height)


pygame.display.update()

pygame.display.update()
while True:
    pygame.event.pump()
    event = pygame.event.wait()

    if event.type == QUIT:
        break
    
    elif event.type == VIDEORESIZE:
        width, height = pygame.display.get_surface().get_size()
        # resize
        # get width and height
        screen.fill((255, 255, 255))
        generate_scene(screen, width, height)
        pygame.display.update()