import RPi.GPIO as GPIO
import time
from random import randint 

leds_ar = [26,19,13,6,5,11,9,10]

rand_ar = []
for i in range (0, 8):
    rand_ar.append(randint(0,1))


GPIO.setmode(GPIO.BCM)
GPIO.setup(leds_ar, GPIO.OUT)
GPIO.output(leds_ar, 0)

number = int(input())

try:
    cnt = 7
    while (number != 0):
        ost = number % 2
        if (ost == 1):
            GPIO.output(leds_ar[cnt], 1)
        cnt -= 1
        number = number // 2
        time.sleep(0.05)
    time.sleep(150)
    
finally:
    GPIO.output(leds_ar, 0)
    GPIO.cleanup()
