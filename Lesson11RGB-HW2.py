'''
Homework 2 for the Use of RGB LED:
Use three toggle switches (push buttons) with corresponding colors to turn the red, green, and blue color on and off.
Have each button as a PWM to make more mixed colors with RGB colors at various dim levels
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

'''
GPIO.output(OutRedPin, 0)
GPIO.output(OutGreenPin, 0)
GPIO.output(OutBluePin, 0)
'''

OutRedPWM = GPIO.PWM(OutRedPin, 1000)
OutGreenPWM = GPIO.PWM(OutGreenPin, 1000)
OutBluePWM = GPIO.PWM(OutBluePin, 1000)

RedState = 0
GreenState = 0
BlueState = 0

RedButtonStateNew = 1
RedButtonStateOld = 1
GreenButtonStateNew = 1
GreenButtonStateOld = 1
BlueButtonStateNew = 1
BlueButtonStateOld = 1

RedDutyCycle = GreenDutyCycle = BlueDutyCycle = 0
OutRedPWM.start(RedDutyCycle)
OutGreenPWM.start(GreenDutyCycle)
OutBluePWM.start(BlueDutyCycle)

try:
	while True:
		RedButtonStateNew = GPIO.input(InRedPin)
		GreenButtonStateNew = GPIO.input(InGreenPin)
		BlueButtonStateNew = GPIO.input(InBluePin)
		#print(RedButtonStateNew, GreenButtonStateNew, BlueButtonStateNew)
		#sleep(1)
		
		if RedButtonStateNew == 1 and RedButtonStateOld == 0:
			RedDutyCycle = RedDutyCycle + 20
			if RedDutyCycle > 100: RedDutyCycle = 0
			OutRedPWM.ChangeDutyCycle(RedDutyCycle)
			print('Go Red!  ', 'Red Duty Cycle = ', RedDutyCycle, '| Green Duty Cycle = ', GreenDutyCycle, '| Blue Duty Cycle = ', BlueDutyCycle)
			sleep(0.05)

		if GreenButtonStateNew == 1 and GreenButtonStateOld == 0:
			GreenDutyCycle = GreenDutyCycle + 20
			if GreenDutyCycle > 100: GreenDutyCycle = 0
			OutGreenPWM.ChangeDutyCycle(GreenDutyCycle)
			print('Go Green!', 'Red Duty Cycle = ', RedDutyCycle, '| Green Duty Cycle = ', GreenDutyCycle, '| Blue Duty Cycle = ', BlueDutyCycle)
			sleep(0.05)
		
		if BlueButtonStateNew == 1 and BlueButtonStateOld == 0:
			BlueDutyCycle = BlueDutyCycle + 20
			if BlueDutyCycle > 100: BlueDutyCycle = 0
			OutBluePWM.ChangeDutyCycle(BlueDutyCycle)
			print('Go Blue! ', 'Red Duty Cycle = ', RedDutyCycle, '| Green Duty Cycle = ', GreenDutyCycle, '| Blue Duty Cycle = ', BlueDutyCycle)
		RedButtonStateOld = RedButtonStateNew
		GreenButtonStateOld = GreenButtonStateNew
		BlueButtonStateOld = BlueButtonStateNew
		sleep(0.05)

except KeyboardInterrupt:  # to exit the program properly while cleaning up the pins
    GPIO.cleanup()
    print(' Bam! GPIO Pins Good to Go!')
