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

def start_info(screen, txt_config, resolution):
    width, height = resolution
    intro_info_txt = [
        txt_config.render("This is P_Types", False, BLACK),
        txt_config.render("You will first be presented with 15 leptons", False, BLACK),
        txt_config.render("Then you will be presented with 15 non-leptons", False, BLACK),
        txt_config.render(" ", False, BLACK),
        txt_config.render("Press any key to continue", False, BLACK),
    ]

    for i in range(len(intro_info_txt)):
        screen.blit(intro_info_txt[i],(width/8,height/4+i*55))

def render_help_txt(screen, txt_config, resolution):
    width, height = resolution
    intro_info_txt = [
        txt_config.render("Are the following pictures Leptons or non-leptons?", False, BLACK),
        txt_config.render("Press Y if it is", False, BLACK),
        txt_config.render("Press N if it isnt", False, BLACK),
        txt_config.render(" ", False, BLACK),
        txt_config.render("Press any key to continue", False, BLACK),
    ]

    for i in range(len(intro_info_txt)):
        screen.blit(intro_info_txt[i],(width/8,height/4+i*55))

def render_help_txt2(screen, txt_config, resolution):
    width, height = resolution
    intro_info_txt = [
        txt_config.render("Is this a lepton?: Y/N", False, BLACK),
    ]

    for i in range(len(intro_info_txt)):
        screen.blit(intro_info_txt[i],(width/3,80))

from itertools import product

class Grid():

    def __init__(self, resolution, shape, matrix):
        self.w = resolution[0]
        self.h = resolution[1]
        self.tiles = matrix
        self.shape = shape
        self.thickness = int(min([self.w/(min(self.shape)*35), self.h/(min(self.shape)*35)]))
        #print(self.tiles.shape)
    
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
            self.draw_borders(centers[c_indx], screen, self.w, self.h)
            self.draw_leptons(centers[c_indx], tile, screen, self.w, self.h, self.thickness)

    def draw_borders(self, centers, screen, w, h):
        size_w = w/(self.shape[0]+0.25*sum(self.shape))
        size_h = h/(self.shape[1]+0.25*sum(self.shape))
        rect = pygame.Rect(centers[0]-size_w/2,centers[1]-size_h/2,size_w,size_h)
        pygame.draw.rect(screen, WHITE, rect)
        return None        

    def draw_leptons(self, centers, plot_vec, screen, w, h, thickness):
        # takes coordinates
        circle(plot_vec[0]*w/(5*self.shape[0]*2)+centers[0], plot_vec[1]*h/(5*self.shape[1]*2)+centers[1], RED, screen, thickness)
        circle(plot_vec[2]*w/(5*self.shape[0]*2)+centers[0], plot_vec[3]*h/(5*self.shape[1]*2)+centers[1], BLUE, screen, thickness)    
        circle(plot_vec[4]*w/(5*self.shape[0]*2)+centers[0], plot_vec[5]*h/(5*self.shape[1]*2)+centers[1], GREEN, screen, thickness)
        # Make relative location scalable with size in such a way, that we can adjust the size of each tile realtive to the overall size of the plot

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

def wait_grid(screen, resolution, grid, progess=2):
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
            if progess == 2:
                render_help_txt2(screen, txt_config, resolution)
            pygame.display.update()
    return resolution, move

def wait(progess, resolution):
    while True:
        pygame.event.pump()
        event = pygame.event.wait()

        if event.type == QUIT:
            exit(0)
        elif event.type == KEYDOWN:
            break
        elif event.type == VIDEORESIZE:
            resolution = screen.get_size()

            if progess == 0:
                screen.fill(GREY)
                start_info(screen, txt_config, resolution)
                pygame.display.update()
            elif progess == 1:
                screen.fill(GREY)
                render_help_txt(screen, txt_config, resolution)
                pygame.display.update()
    
    return resolution

from collections import defaultdict

def main(screen, resolution, txt_config, n_dots=3, lrn_dists=[1.,1.5,2.,2.5], plot_resolution=(5,3)):
    
    progess = 0
    screen.fill(GREY)
    start_info(screen, txt_config, resolution)
    pygame.display.update()
    resolution = wait(progess, resolution)
    screen.fill(GREY)
    ptype = gen_prototype(n_dots)
    

    lrn_lep, non_lep, test_lep = gen_samples(n_dots, lrn_dists, ptype, *plot_resolution)

    # draw info screen <- TODO

    # draw number screen <- get_number function from last week

    # draw the grid for the leptons

    
    grid = Grid(resolution,plot_resolution, lrn_lep)
    grid.draw(screen)
    pygame.display.update()
    resolution, _ = wait_grid(screen,resolution, grid, progess)
    pygame.display.update()
    

    # draw the grid for the non leptons

    
    grid = Grid(resolution,plot_resolution, non_lep)
    grid.draw(screen)
    pygame.display.update()
    resolution, _ = wait_grid(screen, resolution, grid, progess)
    pygame.display.update()

    progess = 1
    screen.fill(GREY)
    render_help_txt(screen, txt_config, resolution)
    pygame.display.update()
    resolution = wait(progess, resolution)
    screen.fill(GREY)
    progess = 2
    # loop through the test cases for the leptons
    
    # The reason for the plus 2 is that we want to iterate over 
    # the lrn_lep and non_lep in our test too
    padded_length = len(lrn_dists)+2
    outer, inner = gen_test_indices(padded_length, plot_resolution)

    outer = iter(outer)
    for i in range(len(inner)):
        inner[i] = iter(inner[i])

    dict_test = np.zeros(len(lrn_dists))
        
    dict_lrn = np.zeros(2) 

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
                    render_help_txt2(screen, txt_config, resolution)
                    pygame.display.update()
                    resolution, move = wait_grid(screen, resolution, grid)
                    if move == Move.Right:                            
                        dict_test[outer_idx] += 1
                elif outer_idx == len(lrn_dists):                        
                    grid = Grid(resolution, (1,1), lrn_lep[inner_idx].reshape(1,6))
                    screen.fill(GREY)
                    grid.draw(screen)
                    render_help_txt2(screen, txt_config, resolution)
                    pygame.display.update()
                    resolution, move = wait_grid(screen, resolution, grid)
                    if move == Move.Right:                            
                        dict_lrn[0] += 1
                elif outer_idx == len(lrn_dists) + 1:
                    grid = Grid(resolution, (1,1), non_lep[inner_idx].reshape(1,6))
                    screen.fill(GREY)
                    grid.draw(screen)
                    render_help_txt2(screen, txt_config, resolution)
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
    width = 800
    height = 800 

    pygame.font.init()
    txt_config = pygame.font.SysFont('Times New Roman', 30)
    pygame.display.set_caption("P_Types")
    pygame.display.init()
    screen = pygame.display.set_mode((width, height),RESIZABLE)

    screen.fill(GREY)
#    main(3,(width,height), [1, 1.5, 2, 2.5], gen_prototype(3), (10, 10), screen)
    main(screen, (width, height), txt_config, 3, [1.,1.5,2.,2.5], (5,3))
