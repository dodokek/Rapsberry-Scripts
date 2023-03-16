import RPi.GPIO as GPIO

def dec2bin(a):
    return [int (digit) for digit in bin(a)[2:].zfill(8)]

def getInput():
    try:
        str = input()
        num = int(str)

        if num < 0:
            print('Емае, ну как я отрицательное то выведу')
            return -1
        elif num > 255:
            print('Подгони больше сведодиодов - тогда поговорим')
            return -1
        else:
            return num

    except Exception:
        if str == "q":
            exit()
        else:
            print("Господи, да введи ты нормальное значение")
            return -1



dac = [26, 13, 19, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while (True):
        print("Enter value from 0 to 255")

        num = getInput()

        if num != -1:
            binary = dec2bin(num)
            GPIO.output(dac, binary)
            print("Volt: ", round(3.3 / 256 * num, 2))
    
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()