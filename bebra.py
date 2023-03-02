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

number = 255

try:
    for i in range(8):
        if rand_ar[i]:
            GPIO.output(leds_ar[i], 1)

    time.sleep(15)
    
finally:
    GPIO.output(leds_ar, 0)
    GPIO.cleanup()
