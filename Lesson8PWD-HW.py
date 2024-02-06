'''
Use 2 push buttons to control the brightness of the LED by 8 steps, from as dim as possible to as bright as possible.  
One button brightens the LED one step each time pressed and the second button dims it. 
You may want to turn it off as the last step for coming down in brightness and turn full on as the highest level. 
'''

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

'''
We will need two input modules to get input from the switches and based on each of the inputs send a PWM command out to the LED.
Let's pick pin 35 and 37 for the two input pins and pin 40 as the output pin via a pulse width modulation as well as pin 39 for ground. 
These assignments should be reversed or reset once the work or project is completed to free up the pins and remove any preset functions assigned to them.
'''
in1 = 35 ; in2 = 37 ; out1 = 40
GPIO.setup(in1, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(in2, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(out1, GPIO.OUT) 
outPWM = GPIO.PWM(out1, 100)

Read1StatOld = 1 ; Read2StatOld = 1 
Read1StatNew = 1 ; Read2StatNew = 1

DutyCycle = 0 ; 
DutyCycleJump = float(input("Please enter a number for the jump in duty cycle between 1 and 99: "))
if DutyCycleJump > 0 and DutyCycleJump < 100:
	print("You are good to use the buttons to brighten or dim the LED with the specified jump in brightness")
	outPWM.start(DutyCycle)
else: 
	print("Invalid Input, setting duty cycle jump to default 15! You are good to go!")
	DutyCycleJump = 15
	outPWM.start(DutyCycle)

try:
	while True:
################### Increasing Brightness
		Read1 = GPIO.input(in1)
		if Read1 == 0:
			Read1StatNew = not Read1StatNew
		if Read1StatOld == 1 and Read1StatNew == 0:
			Read1StatOld = not Read1StatOld
			DutyCycle += DutyCycleJump
			if DutyCycle <=100:
				print('Duty Cycle = ', DutyCycle)
				outPWM.ChangeDutyCycle(DutyCycle)
				sleep(0.2)
			else:
				DutyCycle = 100
				outPWM.ChangeDutyCycle(DutyCycle)
				print('Duty Cycle cannot be more than 100. Setting Duty Cycle to a max of 100 now')
		if Read1 == 1:
			Read1StatOld = 1
			Read1StatNew = 1
################### Decreasing Brightness
		Read2 = GPIO.input(in2)
		if Read2 == 0:
			Read2StatNew = not Read2StatNew
		if Read2StatOld == 1 and Read2StatNew == 0:
			Read2StatOld = not Read2StatOld
			DutyCycle -= DutyCycleJump
			if DutyCycle >= 5:
				print('Duty Cycle = ', DutyCycle)
				outPWM.ChangeDutyCycle(DutyCycle)
				sleep(0.2)
			else:
				DutyCycle = 0
				outPWM.ChangeDutyCycle(DutyCycle)
				print('Duty Cycle cannot be less than 0. Setting Duty Cycle to a min of 0 now')

		if Read1 == 1:
			Read1StatOld = 1
			Read1StatNew = 1
		if Read2 == 1:
			Read2StatOld = 1
			Read2StatNew = 1

except KeyboardInterrupt: # to exit the program properly while cleaning up the pins 
	GPIO.cleanup()
	print('That was it? How quick!')
