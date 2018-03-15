import scrollphathd as sphd
import time
import serial
from random import *
from scrollphathd.fonts import font3x5

test123 = ""

sphd.set_pixel(0,1,0.5)
sphd.show()

for y in range(7):
	sphd.set_pixel(1, y , 0.25)
sphd.show()


test456 = raw_input("Type Something. Then Press Enter\n")
test789 = test456 + ' -'
sphd.clear()

for x in range(17):
	sphd.clear()
	for y in range(7):
		sphd.set_pixel(x, y, 0.25)
	sphd.show()
	time.sleep(1/17.0)
sphd.clear()
sphd.write_string(test789, y=1, font=font3x5, brightness=0.5)

while True:
#	sphd.set_brightness(0.25)
	sphd.show()
	sphd.scroll(1)
	time.sleep(0.13)
