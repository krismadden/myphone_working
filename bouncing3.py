import pygame
from pygame.locals import*

pygame.init()

class Main(object):

	def __init__(self):
		screenSize = (640,480)
		surface = pygame.display.set_mode(screenSize)

		bkg = (140, 220, 200)
		myBox = Box()
		myOtherBox = Box()
		myOtherBox.color = (220, 175, 90)
		myOtherBox.x = 300
		myOtherBox.y = 100
		myOtherBox.vx = 3
		myOtherBox.vy = 5

		while(True):

			surface.fill(bkg)
			myBox.update()
			myOtherBox.update()

			myBox.draw(surface)
			myOtherBox.draw(surface)
			
			pygame.display.flip()

			#function that gets all recently detected input events events
			#this loops through them looking for specific ones
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					pygame.quit()
					quit()

class Box(object):
	def __init__(self):
		self.x = 0
		self.y = 0
		self.vx = 1
		self.vy = 1
		self.size = (50,50)
		self.color = (70,40,100)

	def update(self):
		self.x += self.vx
		self.y += self.vy
	
		if self.x > 640:
			self.vx = -1
		if self.x < 0:
			self.vx = 1
		if self.y > 480:
			self.vy = -1
		if self.y < 0:
			self.vy = 1

	def draw(self, surface):
		rect = pygame.Rect((self.x, self.y), self.size)
		pygame.draw.rect(surface, self.color, rect)

Main()
