#Import libraries
import RPi.GPIO as GPIO
import time
#Define pins
sense = 16 #Pin 36
#5V Power - Pin 2
#Sensor GND - Pin 14
#Define sensor function
def GPIO_callback(sense):
    if GPIO.input(sense):
        print("Input Detected")
    else:
        print("Waiting...")
GPIO.setmode(GPIO.BCM)
GPIO.setup(sense, GPIO.IN)
while True:
    GPIO_callback(sense)
    time.sleep(2)
    