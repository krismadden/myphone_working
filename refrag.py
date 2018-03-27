import time
import serial

#global stuff

numberstring = ""
response = ""
number_kris = "0033637165118"
number = ""

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

print "Initialising Modem.."
serialport = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
response = serialport.readlines(None)
print response
serialport.write("AT+CMEE=2\r")
response = serialport.readlines(None)
print response
serialport.write("AT+CMGF=1\r")
response = serialport.readlines(None)
print response
serialport.write("AT+CSMS=1\r")
response = serialport.readlines(None)
print response
serialport.write("AT+CSCS?\r")
response = serialport.readlines(None)
print response
serialport.write("AT+CSCS=\"GSM\"\r")
response = serialport.readlines(None)
print response
serialport.write("AT+CPIN?\r")
response = serialport.readlines(None)
print response
serialport.write("AT+CPIN=\"1234\"\r")
response = serialport.readlines(None)
print response
serialport.write("AT+COPS=0\r")
response = serialport.readlines(None)
print response
serialport.write("AT+CMGF?\r")
response = serialport.readlines(None)
print response
serialport.write("AT+CMGF=1\r")
response = serialport.readlines(None)
print response
serialport.write("AT+CMGS=\"" + number + "\"\n")
#serialport.write("AT+CMGS=\"0637165118\"<CR>\n")
serialport.write(message+"\r")
serialport.write("\x1A") #ctrlz
response = serialport.readlines(None)
