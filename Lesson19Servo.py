
'''
Objective is control a micro servo motor with the Pi.
The red color is power, using 3.3 v, the brown wire is for ground, and the yellow is for control which goes to a GPIO pin.
We want the period to be 20 ms or 0.02 s. RP takes command in terms of frequency, which is 1/period.
So the frequency would be 1/0.02 = 50 Hz
As for the angle, the ducty cycle dictates (% of time the signal is on) that. 
Somewhere around 1-2% of DC is an angle of 0. 10-15% is an angle of 180 degrees. So it's not between 0 to 100, but from 1 to 15 and need some adjustments while doing it. 
'''

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM) # using broadcom method
pwmPin = 4
GPIO.setup(pwmPin, GPIO.OUT)
pwm = GPIO.PWM(pwmPin, 50)
pwm.start(0)

try:
	while True:
		pwmPercent = float(input("PWM %: "))
		pwm.ChangeDutyCycle(pwmPercent)
		sleep(0.1)
	
	
except KeyboardInterrupt:
	GPIO.cleanup()
	print("GPIO is ready for next task!")
