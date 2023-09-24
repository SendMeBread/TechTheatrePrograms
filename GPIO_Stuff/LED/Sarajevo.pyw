import RPi.GPIO as GPIO
from sys import argv

whichled = argv[1]
rction=argv[2]
                
p1 = 2
p2 = 3
p3 = 4
p4 = 14
p5 = 15
p6 = 17
p7 = 18
p8 = 27
p9 = 22
p10 = 23
p11 = 24
p12 = 10
p13 = 9
p14 = 25
p15 = 11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(p1, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(p2, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(p3, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(p4, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(p5, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(p6, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(p7, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(p8, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(p9, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(p10, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(p11, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(p12, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(p13, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(p14, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(p15, GPIO.OUT)

if rction=="off":
    if whichled=="p1":
        GPIO.output(p1, False)
    if whichled=="p2":
        GPIO.output(p2, False)
    if whichled=="p3":
        GPIO.output(p3, False)
    if whichled=="p4":
        GPIO.output(p4, False)
    if whichled=="p5":
        GPIO.output(p5, False)
    if whichled=="p6":
        GPIO.output(p6, False)
    if whichled=="all":
        GPIO.output(p1, False)
        GPIO.output(p2, False)
        GPIO.output(p3, False)
        GPIO.output(p4, False)
        GPIO.output(p5, False)
        GPIO.output(p6, False)
if rction=="on":
    if whichled=="p1":
        GPIO.output(p1, True)
    if whichled=="p2":
        GPIO.output(p2, True)
    if whichled=="p3":
        GPIO.output(p3, True)
    if whichled=="p4":
        GPIO.output(p4, True)
    if whichled=="p5":
        GPIO.output(p5, True)
    if whichled=="p6":
        GPIO.output(p6, True)
    if whichled=="all":
        GPIO.output(p1, True)
        GPIO.output(p2, True)
        GPIO.output(p3, True)
        GPIO.output(p4, True)
        GPIO.output(p5, True)
        GPIO.output(p6, True)