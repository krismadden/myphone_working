import time
import serial
from random import *


#Global Stuff

numberstring = ""
messages = ["You had me at aloe.", "I'd like to spend more thyme with you", "Please don't ever leaf me.", "Stop. Hammer thyme.", "I'm rooting for you!", "Leaf me alone.", "It's spring. We are so excited we wet our plants!", "I'm awesome, dill with it.", "Say aloe to my little friend.", "I hope thistle cheer you up."]
message = []
response = ""
number_kris = "0033637165118"
number = ""
YorN = ""
end = False
# serialport = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)


def textInfo( ):

	while True:
		number = raw_input("Enter Phone number::\n")

		if number == "Kris" or number == "kris":
			number = number_kris
			print "texting kris..."
			break
		elif len(number) > 13 or len(number) < 10:
			print "Error. Try entering your number in one of the following formats::" + "\n" + "0637165118 +330637165118 or 0033637165118"
			continue
		else:
			break

	message = messages[randint(0, len(messages))]
	
	response = ""
	
	print "Initialising Modem.."
	serialport = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
	serialport.write("AT\r")
	response = serialport.read(None)
	serialport.write("ATE0\r")
	response = serialport.read(None)
	serialport.write("AT\r")
	response = serialport.read(None)
	serialport.write("AT+CMGF=1\r")
	response = serialport.read(None)
	serialport.write("AT+CMGS=\"" + number + "\"\n")
	serialport.write(message+"\r")
	serialport.write("\x1A") #ctrlz
	response = serialport.readlines(None)
	
	if response[1] == "OK\r\n":
		print "Sent!"
	else:
		print "Opps. Error"
		print response
		
	while True:
		YorN = raw_input("Send another message? [y=1/n=2]?\n")
		
		if YorN == "1":
			end = False
			break
		elif YorN == "2":
			end = True
			break
		else:
			print "Error. Type 'y' for yes or 'n' for no and press enter.\n"
			continue
	


textInfo()


while end != True:
	textInfo() 







