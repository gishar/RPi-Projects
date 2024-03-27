import RPi.GPIO as GPIO
import ADC0834
from time import sleep

# since the ADC0834 library uses the Broadcom setting for the GPIO pins, we follow the same scheme
GPIO.setmode(GPIO.BCM)
ADC0834.setup() # this should take care of the setup inside the chip

rLED = 12
gLED = 16
bLED = 20
GPIO.setup(rLED, GPIO.OUT)
GPIO.setup(gLED, GPIO.OUT)
GPIO.setup(bLED, GPIO.OUT)
rPWM = GPIO.PWM(rLED, 1000)
gPWM = GPIO.PWM(gLED, 1000)
bPWM = GPIO.PWM(bLED, 1000)
rDC = 0
gDC = 0
bDC = 0
rPWM.start(rDC)
gPWM.start(gDC)
bPWM.start(bDC)

try:
    while True:
        rVal = ADC0834.getResult(0) # read input from channel 0 on the chip (which has the potentiometer for red color hooked into!)
        gVal = ADC0834.getResult(1) # read input from channel 1 on the chip (which has the potentiometer for red color hooked into!)
        bVal = ADC0834.getResult(2) # read input from channel 2 on the chip (which has the potentiometer for red color hooked into!)
        print(rVal, gVal, bVal)
        
        sleep(1)
        rDC = rVal / 255 * 100
        gDC = gVal / 255 * 100
        bDC = bVal / 255 * 100
        
        #print("rVal = ", rVal, "rDC = ", rDC, "--------", "gVal = ", gVal, "gDC = ", gDC, "--------", "bVal = ", bVal, "bDC = ", bDC)
        rPWM.ChangeDutyCycle(rDC)
        gPWM.ChangeDutyCycle(gDC)
        bPWM.ChangeDutyCycle(bDC)

except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO good to go!')

