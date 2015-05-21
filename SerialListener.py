#!/usr/bin/python

from __future__ import print_function

import os
import serial
import sys

def main():
	# cross platform
	location = ""
	if os.name == "posix": location = "/dev/"

	
	try: # try ubuntu 15 serial setup
		global ser
		ser = serial.Serial(location+'ttyACM0', 9600)
	except serial.serialutil.SerialException:
		print ("Default address not working")

		# handle the case when no plan b
		if sys.argv.__len__() < 1: 
			print ("No argument given for serial port address")
			raise IndexError("Need to specifiy serial port when default doesnt work")
		
		# plan b
		try: 
			global ser
			ser = serial.Serial(location+sys.argv[len(sys.argv) - 1], 9600)
		except serial.serialutil.SerialException: print ("argument given still not working (try ttyACM0 or COM13)")
		except ValueError:
			print ("cant config port, some setting was wrong, yada yada,")
			print (" windows is probably saying some parameter is wrong")
		
		# plan b is go
		else: send()
	# plan a is go
	else: send()

def send():
	while True:
		a = ser.readline()
		if not a == "\n":
			print (a[0], sep = ", ", end=", ")

if __name__ == '__main__':

	main()