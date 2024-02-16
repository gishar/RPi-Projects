'''
Homework for the Use of RGB LED:
Use three toggle switches (push buttons) with corresponding colors to turn the red, green, and blue color on and off
'''

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

InRedPin = 40
InGreenPin = 38
InBluePin = 36
GPIO.setup(InRedPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(InGreenPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(InBluePin, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

OutRedPin = 29
OutGreenPin = 33
OutBluePin = 37
GPIO.setup(OutRedPin, GPIO.OUT)
GPIO.setup(OutGreenPin, GPIO.OUT)
GPIO.setup(OutBluePin, GPIO.OUT)

GPIO.output(OutRedPin, 0)
GPIO.output(OutGreenPin, 0)
GPIO.output(OutBluePin, 0)

RedState = 0
GreenState = 0
BlueState = 0

RedButtonStateNew = 1
RedButtonStateOld = 1
GreenButtonStateNew = 1
GreenButtonStateOld = 1
BlueButtonStateNew = 1
BlueButtonStateOld = 1

try:
	while True:
		RedButtonStateNew = GPIO.input(InRedPin)
		GreenButtonStateNew = GPIO.input(InGreenPin)
		BlueButtonStateNew = GPIO.input(InBluePin)
		
		if RedButtonStateNew == 1 and RedButtonStateOld == 0:
			RedState = not RedState
			GPIO.output(OutRedPin, RedState)
			print('Red Light action!')
		RedButtonStateOld = RedButtonStateNew
		sleep(0.05)

		if GreenButtonStateNew == 1 and GreenButtonStateOld == 0:
			GreenState = not GreenState
			GPIO.output(OutGreenPin, GreenState)
			print('Green Light action!')
		GreenButtonStateOld = GreenButtonStateNew
		sleep(0.05)
		
		if BlueButtonStateNew == 1 and BlueButtonStateOld == 0:
			BlueState = not BlueState
			GPIO.output(OutBluePin, BlueState)
			print('Blue Light action!')
		BlueButtonStateOld = BlueButtonStateNew
		sleep(0.05)

except KeyboardInterrupt:  # to exit the program properly while cleaning up the pins
    GPIO.cleanup()
    print(' Bam! That is it folks!')

