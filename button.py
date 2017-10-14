import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (2,3,4)
white = (255,255,255)
red = (240,10,30)

block_color = (53, 115, 255)

#car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("a bit Racey")
clock = pygame.time.Clock()

#carImg = pygame.draw.rect(gameDisplay, (10,20,100), (100,100,100,100))

