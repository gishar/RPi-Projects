'''
Project 2 : Count in Binary up to 31 using 5 LED (switches)
'''

import RPi.GPIO as GPIO
import numpy as np
from time import sleep

# 1. the GPIO library has to be imported on the machine
# 2. Need to say which numbering convention we're using for the pins, BSM(Broadcom) or Board
# 3. Need to tell the pi whether our pin will function as input or output by providing the number and function.
# In our case, GPIO pin 11 is used to send voltage to the circuit, so it's an output pin.
# This assignment has to be undone once all work/project is completed so the pins will not have a preset function assigned to them.
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
# check this page to summarize the above: https://raspberrypi.stackexchange.com/questions/59583/how-to-write-to-multiple-gpios-at-the-same-time

# Now we can use numbers 1 up to 31 in a for loop to turn the 5 LEDs on as if it is counting the numbers!
n = int(input("Please enter a number less than 32.The 5 LEDs will turn on as if they are counting in Binary up to your number: "))
while n > 31:
    n = int(input("I can only count up to 31! Please enter a number less than or equal to 31: "))
    
for i in np.linspace(1, n, n):
    int1 = i//16 ; mod1=i%16
    int2 = mod1//8 ; mod2= mod1%8
    int3 = mod2//4 ; mod3= mod2%4
    int4 = mod3//2 ; mod4= mod3%2
    int5 = mod4//1 ; mod5= mod4%1
    # print('int1= ', int1) ; print('mod1= ', mod1)
    # print('int2= ', int2) ; print('mod2= ', mod2)
    # print('int3= ', int3) ; print('mod3= ', mod3)
    # print('int4= ', int4) ; print('mod4= ', mod4)
    # print('int5= ', int5) ; print('mod5= ', mod5)
    
    if int1 == 1:
        GPIO.output(29, 1)
    if int2 == 1:
        GPIO.output(31, 1)
    if int3 == 1:
        GPIO.output(33, 1)
    if int4 == 1:
        GPIO.output(35, 1)
    if int5 == 1:
        GPIO.output(37, 1)
    sleep(0.5)
    GPIO.output(29, 0)
    GPIO.output(31, 0)
    GPIO.output(33, 0)
    GPIO.output(35, 0)
    GPIO.output(37, 0)
    sleep(0.5)

# At the very end, we will need to leave a clean slate of the pin so nothing we setup remains
GPIO.cleanup()
