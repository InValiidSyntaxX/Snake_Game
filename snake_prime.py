
#https://www.geeksforgeeks.org/snake-game-in-python-using-pygame-module/+

import pygame
import time
import random

snake_speed = 15

#window size
x = 720
y = 480

#colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# initialize pygame
pygame.init()

#game Window
pygame.display.set_caption ('Snakey Snake')
game_window = pygame.display.set_mode((x,y))

fps = pygame.time.Clock()