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
def GPIO_callback():
    if GPIO.input(sensor):
        print("Close")
        GPIO.output(led, True)
    if not GPIO.input(sensor):
        print("Far")
        GPIO.output(led, False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(led, GPIO.OUT, initial=0)
while True:
    GPIO_callback()
    time.sleep(1)
    try:
        pass
    except KeyboardInterrupt:
        sensor.close()
        led.close()