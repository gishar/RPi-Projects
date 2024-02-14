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
Button1 = 35 ; Button2 = 37 ; LED1 = 40
GPIO.setup(Button1, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(Button2, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(LED1, GPIO.OUT) 
outPWM = GPIO.PWM(LED1, 1000)

Button1StatOld = 1 ; Button2StatOld = 1 
Button1StatNew = 1 ; Button2StatNew = 1

DutyCycle = 1 ; 
outPWM.start(DutyCycle)
print('Press the Buttons to Brighten or Dim the LED')
print('LED will stay on if the Duty Cycle is above 1.0')

# The script below was a modified version of the teacher's solution after I solved it my own way first!
try:
	while True:
################### Increasing Brightness
		Button1StatNew = GPIO.input(Button1)
		Button2StatNew = GPIO.input(Button2)
		if Button1StatOld == 0 and Button1StatNew == 1:
			DutyCycle = DutyCycle*2.0
			if DutyCycle > 100: DutyCycle = 100.0
			print('Brightening Event! Duty Cycle Rounded = ', round(DutyCycle,2))
		if Button2StatOld == 0 and Button2StatNew == 1:
			DutyCycle = DutyCycle/2.0
			#if DutyCycle < 0: DutyCycle = 0.0
			print('Dimming Event! Duty Cycle Rounded = ', round(DutyCycle,2))

		outPWM.ChangeDutyCycle(int(DutyCycle))
		Button1StatOld = Button1StatNew
		Button2StatOld = Button2StatNew
		sleep(0.1)

except KeyboardInterrupt: # to exit the program properly while cleaning up the pins 
	outPWM.stop()
	GPIO.cleanup()
	print('GPIO Pins are good to go!')
