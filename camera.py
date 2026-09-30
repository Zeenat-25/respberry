# Interfacing Raspberry Pi with Pi Camera
#
# Commands:
# sudo apt update
# sudo apt install python3-picamera2 -y
# python3 camera.py
#
# Connection:
# Pi Camera -> Raspberry Pi CSI Camera Port

from picamera2 import Picamera2, Preview
from time import sleep

camera = Picamera2()

config = camera.create_preview_configuration()
camera.configure(config)

camera.start_preview(Preview.QTGL)
camera.start()

sleep(5)

camera.capture_file("image1.jpeg")

camera.stop_preview()
camera.stop()
