import time
import serial

#global stuff

numberstring = ""
response = ""
number_kris = "0033637165118"
number = ""

def readit():
	response = serialport.readlines(None)
	print response
	time.sleep(0.25)   # delays for 5 = 5 seconds 0.5 = 1/2 second.
	
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
readit()

serialport.write("ATE1\r") #helps with rebugging
readit()

serialport.write("AT+CREG=1\r")
readit()

serialport.write("AT+CPIN?\r")
readit()

serialport.write("AT+CPIN=\"1234\"\r")
readit()

#serialport.write("AT+COPS=0\r")
#readit() 

serialport.write("AT+CMEE=2\r")
readit()

serialport.write("AT+CMGF=1\r")
readit()

serialport.write("AT+CSMS=1\r")
readit()

#serialport.write("AT+CSCS?\r")
#readit()

#serialport.write("AT+CSCS=\"GSM\"\r")
serialport.write("AT+CSCS=\"IRA\"\r")
readit()

serialport.write("AT+CSCS?\r")
readit()

#serialport.write("AT+CMGF?\r")
#readit()

serialport.write("AT+CMGF=1\r")
readit()

serialport.write("AT+CMGS=\"" + number + "\"\n")
serialport.write(message+"\r")
#serialport.write("\x1A") #ctrlz
#serialport.write(char.ConvertFromUtf32(26));
serialport.write(chr(26));
#time.sleep(3)
readit()


