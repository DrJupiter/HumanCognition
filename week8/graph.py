from collections import defaultdict
import pygame
import numpy as np
from pygame.constants import KEYDOWN, QUIT, RESIZABLE, VIDEORESIZE

from enum import Enum, unique

from libweek8 import gen_samples, gen_prototype

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,150,0)
GREY = (200, 200, 200)

def circle(x, y, color, screen, thickness):
    pygame.draw.circle(screen,color,(x,y),thickness,thickness) #2 = np.min([x_resolution,y_resolution])

def render_help_txt_info(screen, txt_config, height, width):
    intro_info_txt = [
        txt_config.render("Press \"j\" when you see a target!", False, BLACK),
        txt_config.render("Press \"f\" when you see no target", False, BLACK),
        txt_config.render("Press any key to start the experiment", False, BLACK),
    ]

    for i in range(len(intro_info_txt)):
        screen.blit(intro_info_txt[i],(width/8,height/4+i*55))

from itertools import product

class Grid():

    def __init__(self, resolution, shape, matrix):
        self.w = resolution[0]
        self.h = resolution[1]
        self.tiles = matrix
        self.thickness = int(min([self.w/(min(shape)*35), self.h/min(shape)*35]))
    
    def update_resolution(self, resolution, shape):
        self.w = resolution[0]
        self.h = resolution[1]
        self.h_offset = self.w/(shape[0]+1)
        self.v_offset = self.h/(shape[1]+1)
        self.thickness = int(min([self.w/(min(shape)*35), self.h/min(shape)*35]))

    def get_centers(self, shape):
        self.h_offset = self.w/(shape[0]+1)
        self.v_offset = self.h/(shape[1]+1)
        w_centers = np.linspace(self.h_offset, self.w - self.h_offset, shape[0])
        h_centers = np.linspace(self.v_offset, self.h - self.v_offset, shape[1])
        # an array of (width,height) tuples
        return np.array(list(product(w_centers,h_centers)))

    def draw(self, shape, screen):
        centers = self.get_centers(shape)
        for c_indx, tile in enumerate(self.tiles):
            draw_borders(centers[c_indx], shape, screen, self.w, self.h)
            draw_leptons(centers[c_indx], tile, shape, screen, self.w, self.h, self.thickness)


def draw_borders(centers, shape, screen, w, h):
    size_w = w/(shape[0]+0.25*sum(shape))
    size_h = h/(shape[1]+0.25*sum(shape))
    rect = pygame.Rect(centers[0]-size_w/2,centers[1]-size_h/2,size_w,size_h)
    pygame.draw.rect(screen, WHITE, rect)
    return None        
        
def draw_leptons(centers, plot_vec, shape, screen, w, h, thickness):
    # takes coordinates
    circle(plot_vec[0]*w/(5*shape[0]*2)+centers[0], plot_vec[1]*h/(5*shape[1]*2)+centers[1], RED, screen, thickness)
    circle(plot_vec[2]*w/(5*shape[0]*2)+centers[0], plot_vec[3]*h/(5*shape[1]*2)+centers[1], BLUE, screen, thickness)    
    circle(plot_vec[4]*w/(5*shape[0]*2)+centers[0], plot_vec[5]*h/(5*shape[1]*2)+centers[1], GREEN, screen, thickness)
    # Make relative location scalable with size in such a way, that we can adjust the size of each tile realtive to the overall size of the plot

def wait():
    while True:
        pygame.event.pump()
        event = pygame.event.wait()

        if event.type == QUIT:
            exit(0)
        elif event.type == KEYDOWN:
            break  

def main(n_dots, lrn_dists, p_type, n_v_lrn_plots, n_h_lrn_plots, screen):
    
    learn_samples, non_lep_samples, tests = gen_samples(n_dots, lrn_dists, p_type, n_v_lrn_plots, n_h_lrn_plots)
    grid = Grid((width, height), (n_v_lrn_plots, n_h_lrn_plots) , learn_samples)

    grid.draw((n_v_lrn_plots, n_h_lrn_plots), screen)
    pygame.display.update()

    while True:
        pygame.event.pump()
        event = pygame.event.wait()

        if event.type == QUIT:
            print("exiting")
            exit(0)
        
        elif event.type == VIDEORESIZE:
            #print("fish")
            width_l, height_l = screen.get_size()
            grid.update_resolution((width_l, height_l), (n_v_lrn_plots, n_h_lrn_plots))
            screen.fill(GREY)
            grid.draw((n_v_lrn_plots, n_h_lrn_plots), screen)
            pygame.display.update()


if __name__ == "__main__":
    width = 1000
    height = 800

    pygame.display.set_caption("fishhuner26")
    pygame.display.init()
    screen = pygame.display.set_mode((width, height),RESIZABLE)

    screen.fill(GREY)
    main(3, [1, 1.5, 2, 2.5], gen_prototype(3), 10, 10, screen)
