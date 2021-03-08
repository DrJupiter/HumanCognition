# Copyright Andreas Holme og Klaus Jupiter Bentzen

from collections import defaultdict
import pygame
from pygame.constants import KEYDOWN, QUIT, RESIZABLE, VIDEORESIZE

from libweek5 import generate_cases, generate_comb, check_correctness, calculate_means, bar_plot

BLACK = (0,0,0)
WHITE  = (255, 255, 255)

ACTUAL_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
NUMBERS = "0123456789"

def wait():
    while True:
        pygame.event.pump()
        event = pygame.event.wait()

        if event.type == QUIT:
            exit(0)
        elif event.type == KEYDOWN:
            break                

from copy import deepcopy
def display_letters(input_letters, screen, txt_config, height, width):
    in_copy = deepcopy(input_letters)
    in_copy.insert(0,"!")

    for c in in_copy:
        letter = txt_config.render(f"{c.upper()}", False, BLACK)
        screen.blit(letter,(width/2-20,height/2-60))
        pygame.display.update()
        pygame.time.wait(1000)
        screen.fill(WHITE)
        pygame.display.update()
        pygame.time.wait(200)

def input_letter_display(display_input, screen, txt_config, height, width):
    disp_letters = (txt_config.render(f"{display_input}", False, BLACK))
    
    screen.blit(disp_letters,(width/4,height/2+60))
    pygame.display.update()
    
def render_help_txt(screen, txt_config, height, width):
    intro_info_txt = [
        txt_config.render("Welcome to Free Recall", False, BLACK),
        txt_config.render("A number of letters will be displayed", False, BLACK),
        txt_config.render("Guess these correctly", False, BLACK),
        txt_config.render("By inputting letters, and pressing ENTER to accept your input", False, BLACK),
        txt_config.render("But be precise, your accuracy will be calculated", False, BLACK),
        txt_config.render("", False, BLACK),
        txt_config.render("Press any key to continue", False, BLACK)
    ]

    for i in range(len(intro_info_txt)):
        screen.blit(intro_info_txt[i],(50,height/4+i*45))

def get_number(screen, txt_config, width, height):

    info_txt = txt_config.render("Input the desired number of tests", False, BLACK)
    screen.blit(info_txt,(50,height/2))
    pygame.display.update()

    display_input = ""

    while True:

        pygame.event.pump()
        event = pygame.event.wait()

        if event.type == QUIT:
            exit(0)

        elif event.type == VIDEORESIZE:
            width, height = screen.get_size()

        elif event.type == KEYDOWN:
                    name = pygame.key.name(event.key)
                    if name in NUMBERS:
                        display_input += name.upper()
                        input_letter_display(display_input, screen, txt_config, height, width)
                    elif event.key == pygame.K_BACKSPACE:
                        display_input = display_input[:-1]
                        screen.fill(WHITE)
                        screen.blit(info_txt,(50,height/2))
                        input_letter_display(display_input, screen, txt_config, height, width)
                    elif event.key == pygame.K_RETURN:
                        break
    return int(display_input)

def main(screen, resolution, txt_config, letter_combinations):

    width, height = resolution

    
    position_dict = defaultdict(lambda: 0)

    render_help_txt(screen, txt_config[2], height, width)
    pygame.display.update()
    wait() 
    screen.fill(WHITE)

    for index, case in enumerate(letter_combinations):
        display_input = ""
        display_letters(case, screen, txt_config[1], height, width)

        while True:

            pygame.event.pump()
            event = pygame.event.wait()

            if event.type == QUIT:
                exit(0)

            elif event.type == VIDEORESIZE:
                width, height = screen.get_size()
                txt_config = [pygame.font.SysFont('Times New Roman', int(min([width/20,height/20]))),pygame.font.SysFont('Times New Roman', int(min([width/8,height/8]))),pygame.font.SysFont('Times New Roman', int(min([width/40,height/40])))]
                break
            
            elif event.type == KEYDOWN:
                        name = pygame.key.name(event.key)
                        if name in ACTUAL_ALPHABET:
                            if len(case) >= len(display_input)+1:
                                display_input += name.upper()
                                input_letter_display(display_input, screen, txt_config[0], height, width)
                        elif event.key == pygame.K_BACKSPACE:
                            display_input = display_input[:-1]
                            screen.fill(WHITE)
                            input_letter_display(display_input, screen, txt_config[0], height, width)
                        elif event.key == pygame.K_RETURN:
                            break
        check_correctness(position_dict, case, display_input.lower())
        screen.fill(WHITE)

    bar_plot(calculate_means(position_dict,len(letter_combinations)))


                        

if __name__ == "__main__":
    width = 700
    height = 700


    pygame.display.set_caption("Free Recall")

    pygame.display.init()

    pygame.font.init()
    txt_config_info = pygame.font.SysFont('Times New Roman', 20)
    txt_config_small = pygame.font.SysFont('Times New Roman', 40)
    txt_config_big = pygame.font.SysFont('Times New Roman', 100)

    txt_config = [txt_config_small, txt_config_big, txt_config_info]

    screen = pygame.display.set_mode((width, height),RESIZABLE)

    #number_of_tests = int(input("HOW MANY TESTS DO YOU WANT?: "))
    screen.fill(WHITE)
    pygame.display.update()
    number_of_tests = get_number(screen, txt_config[0], width, height)

    
    cases = generate_cases([10], number_of_tests)
    
    letter_comb = generate_comb(cases)
    
    screen.fill(WHITE)
    pygame.display.update()

    main(screen,(width, height), txt_config, letter_comb)
