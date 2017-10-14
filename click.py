import pygame
import sys
import time

screen = pygame.display.set_mode((640,320))

while True:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if e.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				pygame.quit()
				sys.exit()
		if e.type == pygame.MOUSEBUTTONDOWN:
			mx, my = pygame.mouse.get_pos()
			if my < 160:
				screen.fill((255,0,0))
			else:
				screen.fill((0,109,200))

	time.sleep(0.03)
	pygame.display.update()
