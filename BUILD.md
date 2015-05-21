
Configure AVRDude:
 * `/usr/local/etc/avrdude.conf`
 * or `.avrduderc in ~/`

Build: 
avr-g++\
 -c -g -Os -Wall -fno-exceptions -ffunction-sections -fdata-sections -mmcu=atmega2560 -DF_CPU=16000000L -MMD -DUSB_VID=null -DUSB_PID=null -DARDUINO=105 -D__PROG_TYPES_COMPAT__ -I/usr/share/arduino/hardware/arduino/cores/arduino -I/usr/share/arduino/hardware/arduino/variants/mega /tmp/build8296132296872388448.tmp/ASCIITable.cpp -o /tmp/build8296132296872388448.tmp/ASCIITable.cpp.o

	-Wl --gc-sections // tell compiler to tell linker to not load extra .o objects.

	-c // do not run linker (just make .o(bject) files)
	-g // preserve identifier names for debugging
	-O // for O(ptimization)
	-Wall // W(arn)all
	-fno-exceptions // not allowed to try {} catch () {}
	-ffunction-sections // make 'section .functions' and
	-fdata-sections // '.data' and .function in asm output.
	-mmcu // specify chip (`gcc.gnu.org/onlinedocs/gcc/AVR-Options.html`)
	-DF_CPU // set frequency
	-MMD // something about logging header files
	-DUSB_PID -DUSB_VID // set up voltages
	-DARDUINO // macro for setting ide version
	-D__PROG_TYPES_COMPAT__ // macro for setting Programmer version (?)
	-I // includes
		/usr/share/arduino/hardware/arduino/cores/arduino
		/usr/share/arduino/hardware/arduino/variants/mega
	
	-o /tmp/build8296132296872388448.tmp/ASCIITable.cpp // ouptput

