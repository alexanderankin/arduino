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
		try:
			ser = serial.Serial(location+sys.argv[len(sys.argv) - 1], 9600)
			while True:
				a = ser.readline()
				if not a == "\n":
					print (a[0], sep = ", ", end="")
		except serial.serialutil.SerialException:
			print ("argument given still not working (try ttyACM0 or COM13)")
		except ValueError:
			print ("cant config port, some setting was wrong, yada yada,")
			print (" windows is probably saying some parameter is wrong")


if __name__ == '__main__':

	main()