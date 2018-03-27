#!/usr/bin/python

from m590 import m590

modem = m590()
modem.init()

#SEND SMS
modem.send_sms("+33637165118", "Hello World!")

#READ ALL SMS
modem.read_sms(4)
print modem.SMS

modem.deinit()
