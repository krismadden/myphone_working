#!/usr/bin/python

from m590 import m590
import time

message = ""
number = ""
numberstring = ""
number_kris = "0033637165118"
response = ""
pin = ""

print "Initialising Modem & Checking PIN.."

modem = m590()
modem.init()

while True:
	m590.ser.write("at+cpin?\r")
	response = m590.ser.readlines(None)
	print response

	if response[2] == "+CPIN: READY\r\n" or response[1] == "+CPIN: READY\r\n":
		print "pin okay. let's go."
		break
	elif response[2] == "+CPIN: SIM PIN\r\n":
		pin = raw_input("Enter your SIM's PIN code::\n")
		m590.ser.write("at+cpin=\"" + pin + "\"\r")
		time.sleep(0.5)
		continue
	elif response[2] == "+CPIN: SIM PUK\r\n":
		pin = raw_input("Enter your PUK code::\n")
		m590.ser.write("at+cpin=" + pin)
		continue
	elif response[2] == "+CPIN: SIM PIN2\r\n":
		pin = raw_input("Enter your PIN2 code::\n")
		m590.ser.write("at+cpin=" + pin)
		continue
	elif response[2] == "+CPIN: SIM PUK2\r\n":
		pin = raw_input("Enter your PUK2 code::\n")
		m590.ser.write("at+cpin=" + pin)
		continue
	else:
		print response[2] + "\n"
		print "check your SIM card. If all looks good, get Kris."

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
print "Sending text.."
modem.send_sms(number, message)

response = m590.ser.readlines(None)
if(response[0] == "\n"):
	print "Sent!"
else:
	print response

#READ ALL SMS
#modem.read_sms(4)
#print modem.SMS

modem.deinit()
