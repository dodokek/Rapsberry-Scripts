import RPi.GPIO as GPIO
import time

def dec2bin(a):
    return [int (digit) for digit in bin(a)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac    = [26, 13, 19, 6, 5, 11, 9, 10]
comp   = 4
troechka = 17

GPIO.setup (dac, GPIO.OUT)
GPIO.setup (troechka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup (comp, GPIO.IN)

# перебираем все двоичные значения

def adc():
    for index in range(256):
        bin = dec2bin(index)
        GPIO.output(dac, bin)

        time.sleep(0.005)
        comp_result = GPIO.input(comp)

        if comp_result == 0:
            return index 
    return 0

# Очень пытаемся

try:
    while True:
        indx = adc()
        
        print("Индекс: {:d}".format(indx), "Ура: {:.2f} вольтов".format(3.3 * indx / 256))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()