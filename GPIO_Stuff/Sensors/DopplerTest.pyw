#Import libraries
import RPi.GPIO as GPIO
import time
#Define pins
sensor = 16 #Pin 36
led = 23 #Pin 16
#Sensor 5V Power - Pin 2
#Sensor GND - Pin 14
#LED GND - Pin 34
#Define sensor function
def GPIO_callback_rising(sense):
    GPIO.output(led, True)
    print("Close")
def GPIO_callback_falling(sense):
    GPIO.output(led, False)
    print("Far")

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(led, GPIO.OUT)
GPIO.add_event_detect(sensor, GPIO.RISING, callback=GPIO_callback_rising)
GPIO.add_event_detect(sensor, GPIO.FALLING, callback=GPIO_callback_falling)

try:
    while True:
        pass
except:
    GPIO.cleanup()