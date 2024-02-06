'''
Project 1 : Blink an LED n times
'''

import numpy as np
import time

# 1. the GPIO library has to be imported on the machine
# 2. Need to say which numbering convention we're using for the pins, BSM(Broadcom) or Board
# 3. Need to tell the pi whether our pin will function as input or output by providing the number and function.
# In our case, GPIO pin 11 is used to send voltage to the circuit, so it's an output pin.
# This assignment has to be undone once all work/project is completed so the pins will not have a preset function assigned to them.
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
OutPin = 40
GPIO.setup(OutPin, GPIO.OUT)

# Now we can ask user for the n, the number of times to blink LED and then let it blink!
while True:
	try:
		user_input = input("Enter the number of times to blink LED, or type 'stop' to exit: ")
		n = int(user_input)
	except ValueError:
		if user_input == "stop":
			break
		print("Invalid input!")
		n=0
	
	for i in np.linspace(1, n, n):
		GPIO.output(OutPin, 1)
		time.sleep(0.5)
		GPIO.output(OutPin, 0)
		time.sleep(0.2)
	StopCue = input("Press Enter to play again, or Write 'stop' to finish the blink game: ")
	if StopCue == "stop":
		break
	
	# KeepUp = input("Write 'stop' to finish the blink game, or enter the number of times to blink LED: ") ")
		

# At the very end, we will need to leave a clean slate of the pin so nothing we setup remains
GPIO.cleanup()
