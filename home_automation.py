# IoT Based Home Automation using Raspberry Pi
#
# Commands:
# git clone https://github.com/Zeenat-25/respberry.git
# cd respberry
# sudo apt update
# sudo apt install python3-rpi.gpio -y
# python3 home_automation.py
#
# Connections:
# Relay IN  -> Pin 37 (GPIO26)
# Relay VCC -> Pin 2 (5V)
# Relay GND -> Pin 6 (GND)

import RPi.GPIO as GPIO
from time import sleep

relay_pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

GPIO.output(relay_pin, GPIO.HIGH)

try:
    while True:
        GPIO.output(relay_pin, GPIO.LOW)
        sleep(5)

        GPIO.output(relay_pin, GPIO.HIGH)
        sleep(5)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
