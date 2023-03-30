import RPi.GPIO as GPIO
import time

def dec2bin(a):
    return [int (digit) for digit in bin(a)[2:].zfill(8)]


dac    = [26, 13, 19, 6, 5, 11, 9, 10]
leds   = [21, 20, 16, 12, 7, 8, 25, 24]
comp   = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def adc():
    left = -1
    right = 256

    while 1<3:

        mid  = int((right + left)/2)
        # print(mid)
        GPIO.output(dac, dec2bin(mid))
        time.sleep(0.005)

        comp_val = GPIO.input(comp)
        
        if comp_val == 0:
            right = mid
        else:
            left = mid

        if (right - left <= 1):
            return int(mid)

    return 0

def get_cool_prog_bar(n):

    # if (n > 245):
    #     return [1,1,1,1,1,1,1,1]
    # print(n)


    n   = int((n+5)/256 * 8)
    print(n)

    if n >= 8:
        n = 8
        
    arr = [0]*8

    for index in range(n):
        arr[index] = 1


    return arr

try:
    while True:
        current_val = adc()
        # print(get_cool_prog_bar(0b00010000))
        GPIO.output(leds, get_cool_prog_bar(current_val)) 
        # time.sleep(1)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()