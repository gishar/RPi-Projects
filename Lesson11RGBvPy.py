'''
Use of RGB LED with thee push buttons like previous lesson but this time make it visual using visual python to show a circle showing the colors visually too.
'''
import RPi.GPIO as GPIO
from time import sleep
#import vpython
# p.s. I had a very hard time with this lib and in the end it did not work for me! in RP, it only shows a black box with no shapes in it whether to as for a sphere or a rectangle.
# I decided to change my approach and instead of vpython, use the matplot lib and do the same in a 2D plot!
import numpy
import matplotlib.pyplot as plt

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


#fig, ax = plt.subplots() # Get the current axis (i.e., the current plotting area or subplot)
#circle1 = plt.Circle((0.5, 0.5), 0.3, color = 'black', fill = True)
#ax.add_patch(circle1) # Add the circle1 created before to the plot
#ax.set_aspect('equal', adjustable='box') # Set aspect ratio to be equal (optional)
#plt.show()


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

		if (RedButtonStateNew == 1 and RedButtonStateOld == 0) or (GreenButtonStateNew == 1 and GreenButtonStateOld == 0) or (BlueButtonStateNew == 1 and BlueButtonStateOld == 0):
			ColorRGB = (RedDutyCycle/100, GreenDutyCycle/100, BlueDutyCycle/100)
			ax = plt.gca()
			circle1 = plt.Circle((0.5, 0.5), 0.3, color = ColorRGB, fill = True)
			ax.add_patch(circle1) # Add the circle1 created before to the plot
			ax.set_aspect('equal', adjustable='box') # Set aspect ratio to be equal (optional)
			plt.show()
		
		RedButtonStateOld = RedButtonStateNew
		GreenButtonStateOld = GreenButtonStateNew
		BlueButtonStateOld = BlueButtonStateNew
		sleep(0.05)

except KeyboardInterrupt:  # to exit the program properly while cleaning up the pins
    GPIO.cleanup()
    print(' GPIO Pins Good to Go!')
