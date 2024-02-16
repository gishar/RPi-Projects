'''
Use of RGB LED
'''

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

RedPin = 29
GreenPin = 33
BluePin = 37
GPIO.setup(RedPin, GPIO.OUT)
GPIO.setup(GreenPin, GPIO.OUT)
GPIO.setup(BluePin, GPIO.OUT)

GPIO.output(RedPin, 0)
GPIO.output(GreenPin, 0)
GPIO.output(BluePin, 0)

try:
	while True:
		WhichPin = int(input("LED to light up? 1 for red, 2 for green, and 3 for blue:  "))

		if WhichPin == 1:
			GPIO.output(RedPin, 1)
			GPIO.output(GreenPin, 0)
			GPIO.output(BluePin, 0)
			
		if WhichPin == 2:
			GPIO.output(RedPin, 0)
			GPIO.output(GreenPin, 1)
			GPIO.output(BluePin, 0)
			
		if WhichPin == 3:
			GPIO.output(RedPin, 0)
			GPIO.output(GreenPin, 0)
			GPIO.output(BluePin, 1)

except KeyboardInterrupt: # to exit the program properly while cleaning up the pins 
	GPIO.cleanup()
	print(' That was it? How quick!')
