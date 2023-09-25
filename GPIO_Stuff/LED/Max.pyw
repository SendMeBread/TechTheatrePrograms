import RPi.GPIO as GPIO
from sys import argv

whichled = argv[1]
rction=argv[2]
                
p1 = 17
p2 = 18
p3 = 22
p4 = 23
p5 = 26
p6 = 12
p7 = 20
p8 = 19
p9 = 13
p10 = 5
p11 = 6
p12 = 16
p13 = 21
p14 = 27
p15 = 25
p16 = 24

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
GPIO.setmode(GPIO.BCM)
GPIO.setup(p16, GPIO.OUT)

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
    if whichled=="p7":
        GPIO.output(p7, False)
    if whichled=="p8":
        GPIO.output(p8, False)
    if whichled=="p9":
        GPIO.output(p9, False)
    if whichled=="p10":
        GPIO.output(p10, False)
    if whichled=="p11":
        GPIO.output(p11, False)
    if whichled=="p12":
        GPIO.output(p12, False)
    if whichled=="p13":
        GPIO.output(p13, False)
    if whichled=="p14":
        GPIO.output(p14, False)
    if whichled=="p15":
        GPIO.output(p15, False)
    if whichled=="p16":
        GPIO.output(p16, False)
    if whichled=="all":
        GPIO.output(p1, False)
        GPIO.output(p2, False)
        GPIO.output(p3, False)
        GPIO.output(p4, False)
        GPIO.output(p5, False)
        GPIO.output(p6, False)
        GPIO.output(p7, False)
        GPIO.output(p8, False)
        GPIO.output(p9, False)
        GPIO.output(p10, False)
        GPIO.output(p11, False)
        GPIO.output(p12, False)
        GPIO.output(p13, False)
        GPIO.output(p14, False)
        GPIO.output(p15, False)
        GPIO.output(p16, False)
        
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
    if whichled=="p7":
        GPIO.output(p7, True)
    if whichled=="p8":
        GPIO.output(p8, True)
    if whichled=="p9":
        GPIO.output(p9, True)
    if whichled=="p10":
        GPIO.output(p10, True)
    if whichled=="p11":
        GPIO.output(p11, True)
    if whichled=="p12":
        GPIO.output(p12, True)
    if whichled=="p13":
        GPIO.output(p13, True)
    if whichled=="p14":
        GPIO.output(p14, True)
    if whichled=="p15":
        GPIO.output(p15, True)
    if whichled=="p16":
        GPIO.output(p16, True)
    if whichled=="all":
        GPIO.output(p1, True)
        GPIO.output(p2, True)
        GPIO.output(p3, True)
        GPIO.output(p4, True)
        GPIO.output(p5, True)
        GPIO.output(p6, True)
        GPIO.output(p7, True)
        GPIO.output(p8, True)
        GPIO.output(p9, True)
        GPIO.output(p10, True)
        GPIO.output(p11, True)
        GPIO.output(p12, True)
        GPIO.output(p13, True)
        GPIO.output(p14, True)
        GPIO.output(p15, True)
        GPIO.output(p16, True)