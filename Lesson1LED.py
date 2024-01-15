
'''
Project 1 : turn an LED on and off
'''

# first,the GPIO library has to be imported on the machine
import RPi.GPIO as GPIO

# Need to say which numbering convention we're using for the pins, BSM(Broadcom) or Board
GPIO.setmode(GPIO.BOARD)

# Need to tell the pi whether our pin will function as input or output by providing the number and function.
# In our case, GPIO pin 11 is used to send voltage to the circuit, so it's an output pin.
# This assignment has to be undone once all work/project is completed so the pins will not have a preset function assigned to them.
GPIO.setup(11, GPIO.OUT)

# Now we can turn the LED on, by having the output on the pin set to True (then False! 1 and 0 can also be used)
GPIO.output(11, True)

# In order to put some delay in between running python commands
import time

# Could also make it nicer:
On = True
Off = False
GPIO.output(11, On)
time.sleep(2)  # to delay for 2 sec then:
GPIO.output(11, Off)

# At the very end, we will need to leave a clean slate of the pin so nothing we setup remains
GPIO.cleanup()