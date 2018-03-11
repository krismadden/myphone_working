#!usr/bin/env python

import time
import serial
from random import *
import scrollphathd

#Global Stuff

numberstringKM89 = ""
messagesKM89 = ["You had me at aloe.", 
	    "I'd like to spend more thyme with you", 
	    "Please don't ever leaf me.", 
	    "Stop. Hammer thyme.", 
	    "I'm rooting for you!", 
	    "Leaf me alone.", 
	    "It's spring. We are so excited we wet our plants!", 
	    "I'm awesome, dill with it.", 
	    "Say aloe to my little friend.", 
	    "I hope thistle cheer you up.",
	   "Chive had my eye on you.",
	   "Don't squash my dreams.",
	   "Peas, Love, and Happiness.",
	   "I bean longing for your company.",
	   "I'm meloncholy without you.",
	   "We make a great pear.",
	   "I always have a berry nice time with you.",
	   "Turnip the party!",
	   "Will you rosemary me?",
	   "You're my missing peas.",
	   "This is acorny pun."]
messageKM89 = ""
responseKM89 = ""
number_krisKM89 = "0033637165118"
numberKM89 = ""
YorNKM89 = ""
endKM89 = False


def textInfo( ):

# 	while True:
# 		numberKM89 = raw_input("Enter Phone number::\n")

# 		if numberKM89 == "Kris" or numberKM89 == "kris":
# 			numberKM89 = number_krisKM89
# 			print "texting kris..."
# 			break
# 		elif len(numberKM89) > 13 or len(numberKM89) < 10:
# 			print "Error. Try entering your number in one of the following formats::" + "\n" + "0637165118 +330637165118 or 0033637165118"
# 			continue
# 		else:
# 			break

# 	messageKM89 = messagesKM89[randint(0, len(messagesKM89))] + "\n" + "\n" + "This plant pun was sent to you by the plant phone."

# 	responseKM89 = ""

# 	print "Initialising Modem.."
# 	serialport = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
# 	serialport.write("AT\r")
# 	response = serialport.read(None)
# 	serialport.write("ATE0\r")
# 	response = serialport.read(None)
# 	serialport.write("AT\r")
# 	response = serialport.read(None)
# 	serialport.write("AT+CMGF=1\r")
# 	response = serialport.read(None)
# 	serialport.write("AT+CMGS=\"" + number + "\"\n")
# 	serialport.write(message+"\r")
# 	serialport.write("\x1A") #ctrlz
# 	response = serialport.readlines(None)

# 	if response[1] == "OK\r\n":
# 		print "Sent!"
# 	else:
# 		print "Opps. Error"
# 		print response

# 	while True:
# 		YorNKM89 = raw_input("Send another message? [y=1/n=2]?\n")

# 		if YorNKM89 == "1":
# 			endKM89 = False
# 			break
# 		elif YorNKM89 == "2":
# 			endKM89 = True
# 			break
# 		else:
# 			print "Error. Type '1' for yes or '2' for no and press enter.\n"
# 			continue

for x in range(17):
	scrollphat.clear()
	for y in range(7):
		scrollphat.set_pixel(x, y, 0.25)
	scrollphat.show()
	time.sleep(1/17.0)

textInfo()


while endKM89 != True:
	textInfo()







