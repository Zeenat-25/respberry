# Interfacing Raspberry Pi with RFID using PN532
#
# Commands:
# sudo apt update
# sudo apt install python3-pip python3-smbus i2c-tools -y
# pip3 install adafruit-circuitpython-pn532 --break-system-packages
# sudo raspi-config       # Enable I2C
# sudo i2cdetect -y 1
# python3 rfid.py
#
# Connections:
# PN532 VCC -> Pin 2 (5V)
# PN532 GND -> Pin 6 (GND)
# PN532 SDA -> Pin 3 (GPIO2)
# PN532 SCL -> Pin 5 (GPIO3)
#
# PN532:
# Channel 1 -> ON
# Channel 2 -> OFF

import board
import busio
from adafruit_pn532.i2c import PN532_I2C

i2c = busio.I2C(board.SCL, board.SDA)

pn532 = PN532_I2C(i2c, debug=False)

pn532.SAM_configuration()

print("Place RFID card near the reader...")

while True:
    uid = pn532.read_passive_target(timeout=0.5)

    if uid is not None:
        uid_str = "".join("{:02X}".format(x) for x in uid)
        print("RFID UID:", uid_str)
