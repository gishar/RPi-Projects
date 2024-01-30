'''
Based on the understanding we have of the pull down or pull up resistors, this home work is to use the RP internal voltage source in 
the GPIO setup (pull up resistor); but this time, every time the switch is pressed it will turn the LED on or off. 
The switch will toggle between on and off. 
'''

# first,the GPIO library has to be imported on the machine
import RPi.GPIO as GPIO
# from time import sleep

# Need to say which numbering convention we're using for the pins, BSM(Broadcom) or Board
GPIO.setmode(GPIO.BOARD)

'''
We need to configure the Raspberry Pi to specify whether a particular GPIO pin will function as an input or output. In our specific scenario:
GPIO pin 40 is designated to receive voltage, achieved through an internal Pi pull-up resistor implemented in the code. Therefore, it functions as an input pin. 
We configure GPIO pin 40 using a GPIO setup option to establish a consistent voltage source. We set the voltage to 1, indicating a pull-up resistor is active. 
In this configuration, when the switch is in the "up" position, pin 40 reads a 1. As long as it reads 1, we keep the light off. 
When the switch is pressed, causing pin 40 to detect ground and read a 0, we trigger the output circuit to turn the light on and keep it on even after the switch is released. 
Then the next time switch is pressed, it will have to turn it off, and so on. 

GPIO pin 38 is designated to send voltage, making it an output pin. 
These assignments should be reversed or reset once the work or project is completed to free up the pins and remove any preset functions assigned to them.
'''

Input_Pin = 40
Output_Pin = 38
GPIO.setup(Input_Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(Output_Pin, GPIO.OUT) 
try:
    toggler = 0  # Initializing the variable outside the loop
    while True:
        read_value = GPIO.input(Input_Pin)

        if GPIO.input(Output_Pin) == 0:
            if read_value == 0:
                toggler = 1
            if toggler == 1 and read_value == 1:
                GPIO.output(Output_Pin, 1)

        else:  # if GPIO.input(Output_Pin) == 1:
            if read_value == 0:
                toggler = 0
            if toggler == 0 and read_value == 1:
                GPIO.output(Output_Pin, 0)

except KeyboardInterrupt:  # to exit the program properly while cleaning up the pins
    GPIO.cleanup()
    print(' Bam! That is it folks!')