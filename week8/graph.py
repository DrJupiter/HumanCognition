from collections import defaultdict
import pygame
import numpy as np
from pygame.constants import KEYDOWN, QUIT, RESIZABLE, VIDEORESIZE

from enum import Enum, unique

from libweek8 import gen_samples, gen_prototype, gen_test_indices, plots

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
        self.shape = shape
        self.thickness = int(min([self.w/(min(self.shape)*35), self.h/min(self.shape)*35]))
        print(self.tiles.shape)
    
    def update_resolution(self, resolution):
        self.w = resolution[0]
        self.h = resolution[1]
        self.h_offset = self.w/(self.shape[0]+1)
        self.v_offset = self.h/(self.shape[1]+1)
        self.thickness = int(min([self.w/(min(self.shape)*35), self.h/(min(self.shape)*35)]))

    def get_centers(self):
        self.h_offset = self.w/(self.shape[0]+1)
        self.v_offset = self.h/(self.shape[1]+1)
        w_centers = np.linspace(self.h_offset, self.w - self.h_offset, self.shape[0])
        h_centers = np.linspace(self.v_offset, self.h - self.v_offset, self.shape[1])
        # an array of (width,height) tuples
        return np.array(list(product(w_centers,h_centers)))

    def draw(self, screen):
        centers = self.get_centers()
        for c_indx, tile in enumerate(self.tiles):
            draw_borders(centers[c_indx], self.shape, screen, self.w, self.h)
            draw_leptons(centers[c_indx], tile, self.shape, screen, self.w, self.h, self.thickness)
            
            


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

####################################################################

@unique
class Scene(Enum):
    StartGuide   = 0,
    ControlGuide = 1,
    InfoOne      = 2,
    InfoTwo      = 3,
    Playing      = 4,
    Wrong        = 5,
    Correct      = 6,

def generate_points_learn(resolution, matrix ):
    w, h = resolution

    points = []
    for plot_vec in matrix:
        circle(plot_vec[0], plot_vec[1], RED, w, h, screen)
        circle(plot_vec[2], plot_vec[3], BLUE, w, h, screen)    
        circle(plot_vec[4], plot_vec[5], GREEN, w, h, screen)

    return points

def generate_points_play(resolution, step_size, assignment):

    w, h = resolution

    points = []


    return points

def generate_scene(screen, width, height, step_size, assignment, scene, txt_config):
    screen.fill(WHITE)

    if scene == Scene.Playing:
        place_points(generate_points((width,height), step_size, assignment), width, height, screen, step_size)

    pygame.display.update()

from pygame.constants import K_LSHIFT, K_RSHIFT, K_LCTRL, K_RCTRL, K_LALT, K_RALT, K_LMETA, K_RMETA

MODS = [K_LSHIFT, K_RSHIFT, K_LCTRL, K_RCTRL, K_LALT, K_RALT, K_LMETA, K_RMETA] 

@unique
class Move(Enum):
    Wrong = 0,
    Right = 1,
    Quit  = 2,
    Nothing = 3
    Invalid = 4,

def parse_move_py(event) -> Move:
    if event.key == pygame.K_q:
        return Move.Quit
    elif event.key == pygame.K_y:
        return Move.Right
    elif event.key == pygame.K_n:
        return Move.Wrong
    else:
        if event.key in MODS:
            return Move.Nothing
        return Move.Invalid

def wait():
    while True:
        pygame.event.pump()
        event = pygame.event.wait()

        if event.type == QUIT:
            exit(0)
        elif event.type == KEYDOWN:
            break                

from time import perf_counter, sleep

#############################################

"""
def main(n_dots, lrn_dists, p_type, n_v_lrn_plots, n_h_lrn_plots, screen):
    
    learn_samples, non_lep_samples, tests = gen_samples(n_dots, lrn_dists, p_type, n_v_lrn_plots, n_h_lrn_plots)
    grid = Grid((width, height), (n_v_lrn_plots, n_h_lrn_plots) , learn_samples)

    grid.draw((n_v_lrn_plots, n_h_lrn_plots), screen)
    pygame.display.update()
    wait()

from libweek8 import gen_prototype, gen_samples
"""

def wait_grid(screen, resolution, grid):
    while True:
        pygame.event.pump()
        event = pygame.event.wait()

        if event.type == QUIT:
            exit(0)
        elif event.type == KEYDOWN:
            move = parse_move_py(event)
            break  
        elif event.type == VIDEORESIZE:
            resolution = screen.get_size()
            grid.update_resolution(resolution)
            screen.fill(GREY)
            grid.draw(screen)
            pygame.display.update()
    return resolution, move

from collections import defaultdict

def main(screen, resolution, txt_config, n_dots=3, lrn_dists=[1.,1.5,2.,2.5], plot_resolution=(5,3)):

    ptype = gen_prototype(n_dots)

    lrn_lep, non_lep, test_lep = gen_samples(n_dots, lrn_dists, ptype, *plot_resolution)

    # draw info screen <- TODO

    # draw number screen <- get_number function from last week

    # draw the grid for the leptons

    
    grid = Grid(resolution,plot_resolution, lrn_lep)
    grid.draw(screen)
    pygame.display.update()
    resolution, _ = wait_grid(screen,resolution, grid)
    pygame.display.update()
    

    # draw the grid for the non leptons

    
    grid = Grid(resolution,plot_resolution, non_lep)
    grid.draw(screen)
    pygame.display.update()
    resolution, _ = wait_grid(screen, resolution, grid)
    pygame.display.update()

    # loop through the test cases for the leptons
    
    # The reason for the plus 2 is that we want to iterate over 
    # the lrn_lep and non_lep in our test too
    padded_length = len(lrn_dists)+2
    outer, inner = gen_test_indices(padded_length, plot_resolution)

    outer = iter(outer)
    for i in range(len(inner)):
        inner[i] = iter(inner[i])

    dict_test = defaultdict(lambda: 0)
    for i in range(len(lrn_dists)):
        dict_test[i]
        
    dict_lrn = defaultdict(lambda: 0)
    for i in range(2):
        dict_lrn[i]

    while True:

        outer_idx = next(outer, None)
        if outer_idx == None:
            break            
        else:
            inner_idx = next(inner[outer_idx], None)
            if inner_idx == None:
                break
            else:
                if outer_idx < len(lrn_dists):
                    grid = Grid(resolution, (1,1), test_lep[outer_idx][inner_idx].reshape(1,6))
                    screen.fill(GREY)
                    grid.draw(screen)
                    pygame.display.update()
                    resolution, move = wait_grid(screen, resolution, grid)
                    if move == Move.Right:                            
                        dict_test[outer_idx] += 1
                elif outer_idx == len(lrn_dists):                        
                    grid = Grid(resolution, (1,1), lrn_lep[inner_idx].reshape(1,6))
                    screen.fill(GREY)
                    grid.draw(screen)
                    pygame.display.update()
                    resolution, move = wait_grid(screen, resolution, grid)
                    if move == Move.Right:                            
                        dict_lrn[0] += 1
                elif outer_idx == len(lrn_dists) + 1:
                    grid = Grid(resolution, (1,1), non_lep[inner_idx].reshape(1,6))
                    screen.fill(GREY)
                    grid.draw(screen)
                    pygame.display.update()
                    resolution, move = wait_grid(screen, resolution, grid)
                    if move == Move.Right:                            
                        dict_lrn[1] += 1        

    print(dict_test,dict_lrn)
    plots(dict_lrn, dict_test,[lrn_dists[1],lrn_dists[-1]], lrn_dists, plot_resolution) 
#        pygame.event.pump()
#        event = pygame.event.wait()
#
#        wait()

"""
        if move == Move.Quit:
            print("Exiting")
            exit(0)
        
        elif event.type == VIDEORESIZE:
            width, height = screen.get_size()
"""

if __name__ == "__main__":
    width = 2000
    height = 1000 #int(800*3/5)

    pygame.display.set_caption("fishhuner26")
    pygame.display.init()
    screen = pygame.display.set_mode((width, height),RESIZABLE)

    screen.fill(GREY)
#    main(3,(width,height), [1, 1.5, 2, 2.5], gen_prototype(3), (10, 10), screen)
    main(screen, (width, height), None, 3, [1.,1.5,2.,2.5], (2,2))
