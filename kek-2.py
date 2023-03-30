import RPi.GPIO as GPIO
import time

def dec2bin(a):
    return [int (digit) for digit in bin(a)[2:].zfill(8)]

dac    = [26, 13, 19, 6, 5, 11, 9, 10]
comp   = 4
troechka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup (dac, GPIO.OUT)
GPIO.setup (troechka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup (comp, GPIO.IN)

# Мега бинарный поиск

def adc():
    bin = 0
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
 

# Очень пытаемся

try:
    while True:
        indx = adc()
        print(indx)
        print("Индекс: {:d}".format(indx), "Ура: {:.2f} вольтов".format(3.3 * indx / 256))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()