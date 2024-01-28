'''
Based on the understanding we have of the pull down resistor, the purpose of this homework is to have a switch to turn an LED on with pushing it down.
'''

'''
First let's try to read the input or the incoming signal into GPIO pin 40: 
based on this reading (input circuit), we can command an LED to turn on using an output pin (output circuit)
'''

# first,the GPIO library has to be imported on the machine
import RPi.GPIO as GPIO
from time import sleep

# Need to say which numbering convention we're using for the pins, BSM(Broadcom) or Board
GPIO.setmode(GPIO.BOARD)

'''
Need to tell the pi whether our pin will function as input or output by providing the number and function.
In our case:
GPIO pin 40 is used to receive voltage, so it's an input pin. There is a jumper from pin 1 that provides constant 3.3 v and is controlled by a switch to go to ground. 
Pin 40 is in between, seeing either voltage or ground, depending on the switch. 
GPIO pin 38 is used to send voltage, so it's an output pin.
(These assignments should be undone once all work/project is completed so the pins will not have a preset function assigned to them.)
'''
Input_Pin = 40
Output_Pin = 38
GPIO.setup(Input_Pin, GPIO.IN) 
GPIO.setup(Output_Pin, GPIO.OUT) 

try:
	while True:
		Read_Value = GPIO.input(Input_Pin)
		if Read_Value == 1:
			GPIO.output(Output_Pin, 1)
			print('Light On')
			sleep(1)
		else:
			GPIO.output(Output_Pin, 0)
except KeyboardInterrupt: # to exit the program properly while cleaning up the pins 
	GPIO.cleanup()
	print(' Bam! That is it folks!')

'''
For the pull down resistor:
This is when Pin 40 is connected to ground through a resistor, and connected to pin 1 (voltage source) through a switch.
When the switch is up, all pin 40 sees is ground so it would read 0 and when switch is down, it sees the voltage source and reads a 1, hence the name pull down resistor.
So we can put a condition on when pin 40 reads a 1, then the output pin 38 sends a high voltage to turn an LED on.
'''
