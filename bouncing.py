import pygame

pygame.init()
screenSize_x = 640
screenSize_y = 450
surface = pygame.display.set_mode((screenSize_x, screenSize_y))

#colors
bkg = (170, 220, 221)
blue = (48,77,204)

#surface.fill(bkg)

#box = pygame.Rect((0,0), (50,50))
#pygame.draw.rect(surface, blue, box)

#pygame.display.flip()

#constants
x = 0
y = 0
size = (50,50)
vy = 1
vx = 1

while(True):
#	pass
	surface.fill(bkg)
	
	box = pygame.Rect((x,y),size)
	pygame.draw.rect(surface, blue, box)

	pygame.display.flip()
	
	x += vx
	y += vy

	if x > screenSize_x:
		vx = -1
	if x < 0:
		vx = 1
	if y > screenSize_y:
		vy = -1
	if y < 0:
		vy = 1


	#exit program on Q press
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				pygame.quit()
				quit()
