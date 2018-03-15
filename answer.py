import serial
import time
from sys import exit

number = ""
exit = ""

#while True:
#	number = raw_input("Enter Phone Number::\n")
#
#	if len(number) > 13 or len(number) < 10:
#		print "error. Try entering your number in of  the following formats::"
#		continue
#	else:
#		break

print "initialising Modem.."
#serialport = serial.Serial("/dev/ttyS0", 9600, timeout=0.5)
serialport = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
print "Calling " + number
serialport.write("ATA" + '\r')
response = serialport.readlines(None)
print response


while True:
	exit = raw_input("Press 1 to end call\n")

	if exit == "1":
		break
	else:
		continue

print("Hanging Up...")
serialport.write("AT\r")
response = serialport.readlines(None)
serialport.write("ATH\r")
response = serialport.readlines(None)
print response
