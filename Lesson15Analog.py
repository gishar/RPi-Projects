import RPi.GPIO as GPIO
import ADC0834
from time import sleep

# since the ADC0834 library uses the Broadcom setting for the GPIO pins, we follow the same scheme
GPIO.setmode(GPIO.BCM)
ADC0834.setup() # this should take care of the setup inside the chip

try:
    while True:
        analogVal = ADC0834.getResult(0) # read input from channel 0 on the chip (which has the potentiometer hooked into! Change this and see how it works)
        print(analogVal)
        sleep(0.2)
    

except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO good to go!')