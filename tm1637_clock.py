# ============================================================
# RASPBERRY PI BASED DIGITAL CLOCK USING TM1637
# ============================================================
#
# GITHUB COMMANDS:
#
# Clone repository:
# git clone https://github.com/Zeenat-25/respberry.git
#
# Go inside repository:
# cd respberry
#
# Check files:
# ls
#
#
# INSTALL TM1637 LIBRARY:
#
# Download the TM1637 library:
# wget https://raspberrytips.nl/files/tm1637.py
#
# IMPORTANT:
# The downloaded tm1637.py must be in the same folder
# as this program.
#
#
# RUN PROGRAM:
# python3 tm1637_clock.py
#
#
# ============================================================
# CONNECTIONS:
# ============================================================
#
# TM1637 Display       Raspberry Pi
# -----------------------------------------
# VCC        ------->   Pin 2 (5V)
# GND        ------->   Pin 6 (GND)
# CLK        ------->   Pin 16 (GPIO23)
# DIO        ------->   Pin 18 (GPIO24)
#
# ============================================================


import time
import datetime
import tm1637
import RPi.GPIO as GPIO


# ------------------------------------------------------------
# GPIO PIN CONNECTIONS
# ------------------------------------------------------------

CLK = 23
DIO = 24


# Create TM1637 display object
Display = tm1637.TM1637(
    CLK,
    DIO,
    tm1637.BRIGHT_TYPICAL
)


# Clear display
Display.Clear()


# Set display brightness
Display.SetBrightnes(1)


# ------------------------------------------------------------
# DISPLAY CURRENT TIME
# ------------------------------------------------------------

try:

    while True:

        # Get current date and time
        now = datetime.datetime.now()

        hour = now.hour
        minute = now.minute
        second = now.second


        # Convert time into four digits
        currenttime = [
            int(hour / 10),
            hour % 10,
            int(minute / 10),
            minute % 10
        ]


        # Display HH:MM
        Display.Show(currenttime)


        # Blink colon every second
        Display.ShowDoublepoint(second % 2)


        # Wait for one second
        time.sleep(1)


except KeyboardInterrupt:

    # Clear display when program is stopped
    Display.Clear()

    GPIO.cleanup()

    print("\nDigital Clock Stopped")
