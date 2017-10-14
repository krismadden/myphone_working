import time
#import serial
import pygame
import sys

#to get mouse and key pesses
from pygame.locals import *

pygame.init()

#Global Stuff

numberstring = ""
message = "Hello Kris. From, Kris"
response = ""
number_kris = "0033637165118"
number = ""

#globat GUI
blue = (48, 77, 204)
teal = (148, 207, 211)

screen = pygame.display.set_mode((640,320))
screen.fill(teal)

#print "Initialising Modem.."
#serialport = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
#serialport.write("AT\r")
#response = serialport.readlines(None)
#serialport.write("ATE0\r")
#response = serialport.readlines(None)
#serialport.write("AT\r")
#response = serialport.readlines(None)
#serialport.write("AT+CMGF=1\r")
#response = serialport.readlines(None)

while True:

	number = input("Enter Phone number::\n")

	if number == "Kris" or number == "kris":
		number = number_kris
		print("texting kris...")
		break
	elif len(number) > 13 or len(number) < 10:
		print("Error. Try entering your number in one of the following formats::" + "\n" + "0637165118 +330637165118 or 0033637165118")
		continue
	else:
		break
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if e.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				pygame.quit()
				sys.exit()


message = input("Enter Message::\n")

print("Initialising Modem..")
# serialport = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
# serialport.write("AT\r")
# response = serialport.read(None)
# serialport.write("ATE0\r")
# response = serialport.read(None)
# serialport.write("AT\r")
# response = serialport.read(None)
# serialport.write("AT+CMGF=1\r")
# response = serialport.read(None)
# serialport.write("AT+CMGS=\"" + number + "\"\n")
# serialport.write(message+"\r")
# serialport.write("\x1A") #ctrlz
# response = serialport.readlines(None)





if response[1] == "OK\r\n":
	print("Sent!")
else:
	print("Opps. Error")
	print(response)

#print response
