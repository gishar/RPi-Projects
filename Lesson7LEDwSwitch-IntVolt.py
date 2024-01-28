'''
Based on the understanding we have of the pull down resistor, the purpose of this homework is to have a switch to turn an LED on with pushing it down.
'''

# first,the GPIO library has to be imported on the machine
import RPi.GPIO as GPIO
from time import sleep

# Need to say which numbering convention we're using for the pins, BSM(Broadcom) or Board
GPIO.setmode(GPIO.BOARD)

'''
We need to configure the Raspberry Pi to specify whether a particular GPIO pin will function as an input or output. In our specific scenario:
GPIO pin 40 is designated to receive voltage, achieved through an internal Pi pull-up switch implemented in the code. Therefore, it functions as an input pin. 
We configure GPIO pin 40 using a GPIO setup option to establish a consistent voltage source. By default, we set the voltage to 1, indicating the pull-up switch is active. 
In this configuration, when the switch is in the "up" position, pin 40 reads a 1. As long as it reads 1, we keep the light off. 
When the switch is pressed, causing pin 40 to detect ground and read a 0, we trigger the output circuit to turn the light on.
GPIO pin 38 is designated to send voltage, making it an output pin. 
These assignments should be reversed or reset once the work or project is completed to free up the pins and remove any preset functions assigned to them.
'''
Input_Pin = 40
Output_Pin = 38
GPIO.setup(Input_Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(Output_Pin, GPIO.OUT) 

try:
	while True:
		Read_Value = GPIO.input(Input_Pin)
		
		if Read_Value == 1:
			GPIO.output(Output_Pin, 0)
		else:
			GPIO.output(Output_Pin, 1)
			print('Light On')
			sleep(1)
except KeyboardInterrupt: # to exit the program properly while cleaning up the pins 
	GPIO.cleanup()
	print(' Bam! That is it folks!')
