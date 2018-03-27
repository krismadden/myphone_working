#!/usr/bin/python

from m590 import m590

message = ""
number = ""
numberstring = ""
number_kris = "0033637165118"

modem = m590()
modem.init()

while True:
	number = raw_input("Enter Phone number::\n")

	if number == "Kris" or number == "kris" or number == "KRIS":
		number = number_kris
		print "texting kris..."
		break
	elif len(number) > 13 or len(number) < 10:
		print "Error. Try entering your number in one of the following formatts::" + "\n" + "0637165118 +33637165118 or 0033637165118"
		continue
	else:
		break

message = raw_input("Enter Message::\n")




#SEND SMS
modem.send_sms(number, message)

#READ ALL SMS
#modem.read_sms(4)
#print modem.SMS

modem.deinit()
