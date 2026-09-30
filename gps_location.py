# Raspberry Pi GPS Location System
#
# Commands:
# git clone https://github.com/Zeenat-25/respberry.git
# cd respberry
# sudo apt update
# sudo apt install python3-serial python3-pip -y
# pip3 install pynmea2 --break-system-packages
#
# Enable GPS Serial:
# sudo raspi-config
# Interface Options
# -> Serial Port
# -> Login shell over serial? -> No
# -> Serial port hardware enabled? -> Yes
# -> Finish
# -> Reboot
#
# Check serial port:
# ls -l /dev/serial*
#
# Run:
# python3 gps_location.py
#
# Connections:
# GPS VCC -> Pin 2 (5V)
# GPS GND -> Pin 6 (GND)
# GPS TX  -> Pin 10 (GPIO15 / RXD)
# GPS RX  -> Pin 8 (GPIO14 / TXD)

import serial
import pynmea2

PORT = "/dev/serial0"
BAUD = 9600

try:
    gps = serial.Serial(PORT, BAUD, timeout=1)

    print("GPS Connected")
    print("Waiting for GPS data...")

    while True:
        line = gps.readline().decode("ascii", errors="ignore").strip()

        if line.startswith(("$GPGGA", "$GNGGA")):
            try:
                data = pynmea2.parse(line)

                if data.latitude != 0 and data.longitude != 0:
                    print("\nGPS LOCATION")
                    print("Latitude :", data.latitude)
                    print("Longitude:", data.longitude)
                    print("Altitude :", data.altitude, "meters")
                    print("Satellites:", data.num_sats)
                    print("UTC Time :", data.timestamp)

            except pynmea2.ParseError:
                pass

except KeyboardInterrupt:
    print("\nGPS Stopped")

except Exception as e:
    print("GPS Error:", e)

finally:
    if "gps" in locals() and gps.is_open:
        gps.close()
