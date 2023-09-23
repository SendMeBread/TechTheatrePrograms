import RPi.GPIO as GPIO
import time
from sys import argv
pause = time.sleep
whichled = argv[1]
rction=argv[2]

r = 17
g = 18
y = 22
b = 23
o = 25
w = 9

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(r, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(g, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(y, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(b, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(o, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(w, GPIO.OUT)

if rction=="off":
    if whichled=="r":
        GPIO.output(r, False)
    if whichled=="g":
        GPIO.output(g, False)
    if whichled=="y":
        GPIO.output(y, False)
    if whichled=="b":
        GPIO.output(b, False)
    if whichled=="o":
        GPIO.output(o, False)
    if whichled=="w":
        GPIO.output(w, False)
    if whichled=="all":
        GPIO.output(r, False)
        GPIO.output(g, False)
        GPIO.output(y, False)
        GPIO.output(b, False)
        GPIO.output(o, False)
        GPIO.output(w, False)
if rction=="on":
    if whichled=="r":
        GPIO.output(r, True)
    if whichled=="g":
        GPIO.output(g, True)
    if whichled=="y":
        GPIO.output(y, True)
    if whichled=="b":
        GPIO.output(b, True)
    if whichled=="o":
        GPIO.output(o, True)
    if whichled=="w":
        GPIO.output(w, True)
    if whichled=="all":
        GPIO.output(r, True)
        GPIO.output(g, True)
        GPIO.output(y, True)
        GPIO.output(b, True)
        GPIO.output(o, True)
        GPIO.output(w, True)