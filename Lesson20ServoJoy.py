
'''
Objective is control a micro servo motor with a joystick which is basically a couple potentiometer and a push button.
For the servo, I connect the red color is 3.3 v pin, the brown wire to ground, and the yellow to a GPIO pin to control the motor, which will be getting input based on the joystick positions.
For the Servo motor, we want the period to be 20 ms or 0.020 s. RP takes command in terms of frequency, which is 1/period. So the frequency would be 1/0.02 = 50 Hz
As for the angle, the duty cycle (DC) dictates (% of time the signal is on) that. 
Somewhere around 1-2% of DC is an angle of 0. 10-15% is an angle of 180 degrees. So it's not between 0 to 100, but from 1 to 15 and need some adjustments while doing it. 
'''

import RPi.GPIO as GPIO
import ADC0834
from time import sleep

# since the ADC0834 library uses the Broadcom setting for the GPIO pins, we follow the same scheme
GPIO.setmode(GPIO.BCM) # using broadcom method
ADC0834.setup() # this should take care of the setup inside the chip

PushPin = 21 # this is for the push pin for the joystick (although it may not be used in this setting top move a servo!)
pwmPin = 4 # this is to be used for ordering the servo to move by a certin degree based on the info received from the joystick
GPIO.setup(PushPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # for a refresher on built-in pull-up resistor, see Lesson7LEDSwitch-IntVolt.py
GPIO.setup(pwmPin, GPIO.OUT)
pwm = GPIO.PWM(pwmPin, 50)
pwm.start(0)

try:
	while True:
		analogValX = ADC0834.getResult(0) # read input from channel 0 on the chip (which has the joystick x-direction reading, 0 to 255; it's a potentiometer afterall!)
		analogValY = ADC0834.getResult(1) # read input from channel 1 on the chip (which has the joystick y-direction reading, 0 to 255; it's a potentiometer afterall!)
		PushButtonState = GPIO.input(PushPin)
		#print(analogValX, analogValY, PushButtonState)
		sleep(0.1)
    
		pwmPercent = analogValX*10/255+2
		#print(analogValX, pwmPercent)
		pwm.ChangeDutyCycle(pwmPercent)
		sleep(0.1)
	
	
except KeyboardInterrupt:
	GPIO.cleanup()
	print("GPIO is ready for next task!")

