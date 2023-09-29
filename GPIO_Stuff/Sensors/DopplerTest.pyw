#Import libraries
import RPi.GPIO as GPIO
#Define pins
led = 27 #Pin 14
sense = 16 #Pin 36
#5V Power - Pin 2
#Sensor GND - Pin 14
#LED GND - Pin 34
#Define sensor function
def GPIO_callback(sense):
    if GPIO.input(sense):
        GPIO.output(led, True)
    else:
        GPIO.output(led, False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(sense, GPIO.IN)
GPIO.setup(led, GPIO.OUT)