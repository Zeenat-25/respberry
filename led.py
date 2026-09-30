# SETUP - GND - 6 , VCC - 5 


import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(5, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)

numTimes = int(input("Enter total number of times to blink: "))
speed = float(input("Enter blink speed in seconds: "))

for i in range(numTimes):

    GPIO.output(5, True)
    GPIO.output(10, True)
    GPIO.output(19, True)
    GPIO.output(26, True)
    GPIO.output(29, True)

    print("Iteration", i + 1)
    time.sleep(speed)

    GPIO.output(29, False)
    GPIO.output(26, False)
    GPIO.output(19, False)
    GPIO.output(10, False)
    GPIO.output(5, False)

    time.sleep(speed)

print("Done")

GPIO.cleanup()
