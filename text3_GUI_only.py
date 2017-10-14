import time
#import serial
import pygame
import sys

#to get mouse and key pesses
from pygame.locals import *




#globat GUI
blue = (48, 77, 204)
tealz = (148, 207, 211)

screen = pygame.display.set_mode((420,640))
screen.fill(tealz)
pygame.display.update()


while True:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if e.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				pygame.quit()
				sys.exit()


