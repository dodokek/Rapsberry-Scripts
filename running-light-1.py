import RPi.GPIO as GPIO
import time


leds_ar = [21,20,16,12,7,8,25,24]
GPIO.setmode(GPIO.BCM)

GPIO.setup(leds_ar, GPIO.OUT)
GPIO.output(leds_ar, 0)
try:
    for i in range(4):
        for led in leds_ar:
            GPIO.output(led, 1)
            time.sleep(0.2)
            GPIO.output(led, 0)
finally:
    GPIO.output(leds_ar, 0)
    GPIO.cleanup()
