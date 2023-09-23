import gpiozero
import time
LED = gpiozero.LED
pause = time.sleep

red1 = gpiozero.PWMLED(17)

while True:
    red1.value = 0
    pause(0.5)
    red1.value = 0.25
    pause(0.5)
    red1.value = 0.5
    pause(0.5)
    red1.value = 0.75
    pause(0.5)
    red1.value = 1
    pause(1.25)