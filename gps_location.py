# ============================================================
# RASPBERRY PI GPS LOCATION SYSTEM
# ============================================================
#
# GITHUB COMMANDS:
#
# git clone https://github.com/Zeenat-25/respberry.git
#
# cd respberry
#
# Install required library:
# pip3 install pynmea2
#
# Enable Serial:
# sudo raspi-config
#
# Interface Options
# -> Serial Port
# -> Enable Serial Interface
#
# Check GPS port:
# ls /dev/serial*
#
# Run program:
# python3 gps_location.py
#
#
# ============================================================
# GPS CONNECTIONS (NEO-6M GPS MODULE)
# ============================================================
#
# GPS VCC  ---> Raspberry Pi Pin 2 (5V)
#
# GPS GND  ---> Raspberry Pi Pin 6 (GND)
#
# GPS TX   ---> Raspberry Pi Pin 10 (GPIO15 RXD)
#
# GPS RX   ---> Raspberry Pi Pin 8  (GPIO14 TXD)
#
# ============================================================


import serial
import pynmea2
import time


# GPS Serial Port
GPS_PORT = "/dev/serial0"

# GPS baud rate
BAUD_RATE = 9600


try:

    gps = serial.Serial(
        GPS_PORT,
        baudrate=BAUD_RATE,
        timeout=1
    )

    print("GPS Connected")
    print("Waiting for satellite data...")


except Exception as e:

    print("GPS Connection Error:")
    print(e)

    exit()



while True:

    try:

        data = gps.readline().decode(
            "ascii",
            errors="replace"
        )


        # Check GPS location sentence
        if data.startswith("$GPGGA"):

            msg = pynmea2.parse(data)


            latitude = msg.latitude
            longitude = msg.longitude


            print("--------------------------------")
            print("GPS LOCATION")
            print("--------------------------------")

            print("Latitude :", latitude)

            print("Longitude:", longitude)

            print("Altitude :", msg.altitude, "meters")

            print("Satellites:", msg.num_sats)

            print("UTC Time :", msg.timestamp)

            print("--------------------------------")


            time.sleep(2)


    except pynmea2.ParseError:

        pass


    except KeyboardInterrupt:

        print("\nGPS Stopped")

        gps.close()

        break
