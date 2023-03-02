import RPi.GPIO as GPIO
import time
from random import randint 

leds_ar = [26,19,13,6,5,11,9,10]
aux_ar =  [22,23,27,18,15,14,3,2]

rand_ar = []
for i in range (0, 8):
    rand_ar.append(randint(0,1))


GPIO.setmode(GPIO.BCM)
GPIO.setup(leds_ar, GPIO.OUT)
GPIO.setup(aux_ar, GPIO.IN)
GPIO.output(leds_ar, 1)


try:
    while(1):
        for i in range(0,8):
            
            GPIO.output(leds_ar[i], GPIO.input(aux_ar[i]) )
            

        time.sleep(0.2)
    
finally:
    GPIO.output(leds_ar, 0)
    GPIO.cleanup()
