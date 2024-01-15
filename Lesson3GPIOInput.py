
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

# first,the GPIO library has to be imported on the machine
import RPi.GPIO as GPIO

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
Read_Value = GPIO.input(Input_Pin)
print('GPIO Input: ', Read_Value)

# try hooking to GPIO 39, which is ground, instead of pin 1 with 3.3 v output then run the code. You shoud read a 0 this time

'''
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
'''

# At the very end, we will need to leave a clean slate of the pin so nothing we setup remains
GPIO.cleanup()
