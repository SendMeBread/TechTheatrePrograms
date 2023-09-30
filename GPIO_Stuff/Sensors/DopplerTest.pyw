#Import libraries
import RPi.GPIO as GPIO
import time
#Define pins
sense = 16 #Pin 36
led = 23 #Pin 16
#Sensor 5V Power - Pin 2
#Sensor GND - Pin 14
#LED GND - Pin 34
#Define sensor function
def GPIO_callback(sense):
    if GPIO.input(sense):
        print("Input Detected")
        GPIO.output(led, True)
    else:
        print("Waiting...")
        GPIO.output(led, False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sense, GPIO.IN)
while True:
    GPIO_callback(sense)
    if KeyboardInterrupt:
        GPIO.cleanup()
    time.sleep(2)