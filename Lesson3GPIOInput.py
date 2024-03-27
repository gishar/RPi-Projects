
'''
Project 3 : Understanding GPIO Inputs and Pull Up and Pull Down Resistors
'''

'''
First let's try to read the input or the incoming signal into a GPIO pin:
1. Grab a female to female jumper and hook a female to GPIO 40, and the other female to GPIO 1 for the 3.3 v output 
(never do this on pin 2 which is 5 v! that will fry the pi)
2. let's read this signal on GPIO 40 coming from GPIO 1. In this digital world, a 3.3 v counts as a 1 (on) and lower than that is a 0 (off or false). 
So if we read correctly, we should read a 1.
'''

input("This will read the digital input into Pin 40. Press Enter to Start. Press Ctrl + C to Stop")

# first,the GPIO library has to be imported on the machine
import RPi.GPIO as GPIO
from time import sleep

# Need to say which numbering convention we're using for the pins, BSM(Broadcom) or Board
GPIO.setmode(GPIO.BOARD)

'''
Need to tell the pi whether our pin will function as input or output by providing the number and function.
In our case, GPIO pin 40 is used to receive voltage, so it's an input pin. 
(This assignment has to be undone once all work/project is completed so the pins will not have a preset function assigned to them.)
Then we read the input.
'''
Input_Pin = 40
GPIO.setup(Input_Pin, GPIO.IN)
try:
	while True:
		Read_Value = GPIO.input(Input_Pin)
		print('GPIO Input: ', Read_Value)
		sleep(0.2)
except KeyboardInterrupt: # to exit the program properly while cleaning up the pins 
	GPIO.cleanup()
	
'''
while loop is used to let it run continuously, but to let keyboard interrupt get out of it, the whole loop is put inside a try/except.
when it comes into the except condition, it wil clean the slate of the GPIO pins for the next round of calls
try hooking to GPIO 39, which is ground, instead of pin 1 with 3.3 v output then run the code. You shoud read a 0 this time
try no hooking to 39 or 1: this is a floating input and you might get a 0 or a 1. Not Good! 
and this is why we need a pullup or pulldown resister with a push button to change signals instead of hoking and unhooking.

For a pull up resistor:
Pin 40 is connected to Pin 1 through a 10k ohm resistor and connected to ground through a switch. 
When the switch is up, pin 40 see the voltage from pin 1 and reads 1 since there is no current going anywhere.
When switch is down, the voltage from pin 1 sees ground and current flows, so pin 40 will read a 0.
The above, when the switch is up it reads 1 so it's a pull up resistor.

For the pull down resistor:
This is when Pin 40 is connected to ground through a resistor, and connected to pin 1 (voltage source) through a switch.
When the switch is up, all pin 40 sees is ground so it would read 0 and when switch is down, current flows and it reads a 1, hence the name pull down resistor
'''
