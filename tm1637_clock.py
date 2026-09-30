# Raspberry Pi Based Digital Clock Using TM1637
#
# Commands:
# git clone https://github.com/Zeenat-25/respberry.git
# cd respberry
# ls
# wget https://raspberrytips.nl/files/tm1637.py
# python3 tm1637_clock.py
#
# Connections:
# TM1637 VCC -> Pin 2 (5V)
# TM1637 GND -> Pin 6 (GND)
# TM1637 CLK -> Pin 16 (GPIO23)
# TM1637 DIO -> Pin 18 (GPIO24)

import time
import datetime
import tm1637
import RPi.GPIO as GPIO

CLK = 23
DIO = 24

display = tm1637.TM1637(
    CLK,
    DIO,
    tm1637.BRIGHT_TYPICAL
)

display.Clear()
display.SetBrightnes(1)

try:
    while True:
        now = datetime.datetime.now()

        hour = now.hour
        minute = now.minute
        second = now.second

        current_time = [
            hour // 10,
            hour % 10,
            minute // 10,
            minute % 10
        ]

        display.Show(current_time)
        display.ShowDoublepoint(second % 2)

        time.sleep(1)

except KeyboardInterrupt:
    display.Clear()
    GPIO.cleanup()
    print("Digital Clock Stopped")
