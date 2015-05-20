#!/usr/bin/python

from __future__ import print_function

import os
import serial
import sys
def main():
	# cross platform
	location = ""
	if os.name == "posix": location = "/dev/"

	if sys.argv.__len__() < 1:
		print ("No argument given for serial port address")
	try:
		ser = serial.Serial(location+'ttyACM0', 9600)
		while True:
			a = ser.readline()
			if not a == "\n":
				print (a[0], sep = ", ", end="")
	except serial.serialutil.SerialException:
		print ("Default address not working")

		

if __name__ == '__main__':
	
	main()