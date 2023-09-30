#Import libraries
import RPi.GPIO as GPIO
import time
#Define pins
sensor = 16 #Pin 36
led = 23 #Pin 16
E_Magnet = 26
#Sensor 5V Power - Pin 2
#Sensor GND - Pin 14
#LED GND - Pin 34
#E-Magnet 3.3V Power - Pin 1
#E-Magnet GND - Pin 9
#Define sensor function
def GPIO_callback():
    if GPIO.input(sensor):
        print("Close")
        GPIO.output(led, True)
        GPIO.output(E_Magnet, True)
    if not GPIO.input(sensor):
        print("Far")
        GPIO.output(led, False)
        GPIO.output(E_Magnet, False)
        
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(led, GPIO.OUT, initial=0)
GPIO.setup(E_Magnet, GPIO.OUT, initial=0)
while True:
    time.sleep(2)
    GPIO_callback()
    try:
        pass
    except KeyboardInterrupt:
        sensor.close()
        led.close()