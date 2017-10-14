import pygame
from pygame.locals import*
from pygame import gfxdraw

import time

pygame.init()

#globat GUI
blue = (48, 77, 204)
blue_hover = (68, 87, 214)
blue_press = (78, 97, 224)
teal = (148, 207, 211)




class Main(object):

	def __init__(self):
		global surface
		screenSizeX = 420
		screenSizeY = 640
		screenSize = (screenSizeX,screenSizeY)
		surface = pygame.display.set_mode(screenSize)

		while(True):

			surface.fill(teal)

			for i in range(12):
				x=0
				y=0
				w=90
				h=w
				spacing= w*1.25
				leftoffset = (screenSizeX - w*3 - spacing*2 + w*2)/2
				topoffset = (screenSizeY - h*4 - spacing*3 + h*3)/2
				if -1 < i < 3:
					x = i * spacing + w * 0.5 + leftoffset
					y = 0 * spacing + h * 0.5 + topoffset
					button(str(i+1), x, y, w, h, blue, blue_hover, str(i+1))
				elif 2 < i < 6:
					x = (i-3) * spacing + w * 0.5 + leftoffset
					y = 1 * spacing + h * 0.5 + topoffset
					button(str(i+1), x, y, w, h, blue, blue_hover, str(i+1))
				elif 5 < i < 9:
					x = (i-6) * spacing + w * 0.5 + leftoffset
					y = 2 * spacing + h * 0.5 + topoffset
					button(str(i+1), x, y, w, h, blue, blue_hover, str(i+1))
				elif 8 < i < 12:
					x = (i-9) * spacing + w * 0.5 + leftoffset
					y = 3 * spacing + h * 0.5 + topoffset
					if i == 9:
						button("*", x, y, w, h, blue, blue_hover, "*")
					elif i == 10:
						button("0", x, y, w, h, blue, blue_hover, "0")
					elif i == 11:
						button("#", x, y, w, h, blue, blue_hover, "#")

			
			pygame.display.flip()

			#function that gets all recently detected input events events
			#this loops through them looking for specific ones
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					pygame.quit()
					quit()

def button(msg,x,y,w,h,inactiveCol, activeCol, action=None):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w/2 > mouse[0] > x-w/2 and y+h/2 > mouse[1] > y-h/2:
        #pygame.draw.ellipse(surface, inactiveCol, (x,y,w,h))
        #filled_circle(surface, x, y, r, color)
        pygame.gfxdraw.filled_circle(surface, int(x), int(y), int(w/2), inactiveCol)

    	#aacircle(surface, x, y, r, color)
        pygame.gfxdraw.aacircle(surface, int(x), int(y), int(w/2), (255,255,255))
        if click[0] == 1 and action != None:
            delay = 0.2
            if action == "1":
                print("1")
                time.sleep(delay)
            elif action == "2":
                print("2")
                time.sleep(delay)
            elif action == "3":
                print("3")
                time.sleep(delay)
            elif action == "4":
                print("4")
                time.sleep(delay)
            elif action == "5":
                print("5")
                time.sleep(delay)
            elif action == "6":
                print("6")
                time.sleep(delay)
            elif action == "7":
                print("7")
                time.sleep(delay)
            elif action == "8":
                print("8")
                time.sleep(delay)
            elif action == "9":
                print("9")
                time.sleep(delay)
            elif action == "*":
                print("*")
                time.sleep(delay)
            elif action == "0":
                print("0")
                time.sleep(delay)
            elif action == "#":
                print("#")
                time.sleep(delay)


    else:
    	#filled_circle(surface, x, y, r, color)
    	#pygame.gfxdraw.filled_circle(surface, int(x), int(y), int(w/2), activeCol)

    	#aacircle(surface, x, y, r, color)
    	pygame.gfxdraw.aacircle(surface, int(x), int(y), int(w/2), (255,255,255))
    	


    smallText = pygame.font.Font("freesansbold.ttf", 20)
    medText = pygame.font.Font("freesansbold.ttf", 40)
    textSurf, textRect = text_objects(msg,medText)
    textRect.center = (x,y)
    surface.blit(textSurf, textRect)

def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

Main()

