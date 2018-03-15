#!usr/bin/env python

import time
import serial
from random import *
import scrollphathd as sphd

for x in range(17):
	sphd.clear()
	for y in range(7):
		sphd.set_pixel(x, y, 0.25)
	sphd.show()
	time.sleep(1/17.0)
