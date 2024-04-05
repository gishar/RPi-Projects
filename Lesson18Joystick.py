import RPi.GPIO as GPIO
import ADC0834
from time import sleep

# since the ADC0834 library uses the Broadcom setting for the GPIO pins, we follow the same scheme
GPIO.setmode(GPIO.BCM)
ADC0834.setup() # this should take care of the setup inside the chip

PushPin = 21
GPIO.setup(PushPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # for a refresher on built-in pull-up resistor, see Lesson7LEDSwitch-IntVolt.py

try:
    while True:
        analogValX = ADC0834.getResult(0) # read input from channel 0 on the chip (which has the joystick x-direction reading, 0 to 255; it's a potentiometer afterall!)
        analogValY = ADC0834.getResult(1) # read input from channel 1 on the chip (which has the joystick y-direction reading, 0 to 255; it's a potentiometer afterall!)
        PushButtonState = GPIO.input(PushPin)
        print(analogValX, analogValY, PushButtonState)
        sleep(0.1)
    
except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO good to go!')