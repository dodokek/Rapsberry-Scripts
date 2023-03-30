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
    bin = 0
    for index in range(7, -1, -1):
        bin += 2**(index)               # Соответствующий разряд в единицу и сравниваем

        GPIO.output(dac, dec2bin(bin))
        time.sleep(0.005)

        comp_val = GPIO.input(comp)
        
        if comp_val == 0:
            bin -= 2**(index)
    return bin

def get_cool_prog_bar(n):

    # if (n > 245):
    #     return [1,1,1,1,1,1,1,1]
    # print(n)

    n  = int( (n/256) * 10 )

    bin_arr = dec2bin(n)

    print(bin_arr)

    for i in range(0, 8):
        if bin_arr[i] == 1:
            for j in range(i, 8):
                bin_arr[j] = 1
            # print(bin_arr)
            return bin_arr
    # print(bin_arr)

    return bin_arr

try:
    while True:
        current_val = adc()
        # print(get_cool_prog_bar(0b00010000))
        GPIO.output(leds, get_cool_prog_bar(current_val)) 
        # time.sleep(1)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()