# Raspberry Pi Based Oscilloscope
#
# Commands:
# git clone https://github.com/Zeenat-25/respberry.git
# cd respberry
# sudo apt update
# sudo apt install python3-dev python3-smbus python3-matplotlib git -y
# git clone https://github.com/adafruit/Adafruit_Python_ADS1x15.git
# cd Adafruit_Python_ADS1x15
# sudo python3 setup.py install
# cd ..
# pip3 install drawnow --break-system-packages
# python3 oscilloscope.py
#
# Connections:
# ADS1115 VCC -> Pin 17 (3.3V)
# ADS1115 GND -> Pin 6 (GND)
# ADS1115 SDA -> Pin 3 (GPIO2/SDA)
# ADS1115 SCL -> Pin 5 (GPIO3/SCL)
# Signal -> ADS1115 A0
# Signal GND -> ADS1115 GND

import time
import matplotlib.pyplot as plt
from drawnow import drawnow
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1
values = []

plt.ion()


def plot_graph():
    plt.title("Raspberry Pi Based Oscilloscope")
    plt.xlabel("Time")
    plt.ylabel("ADC Value")
    plt.grid(True)
    plt.plot(values)


print("Oscilloscope Started...")
print("Reading ADS1115 Channel 0")

while True:
    adc_value = adc.read_adc(0, gain=GAIN)

    print("ADC Value:", adc_value)

    values.append(adc_value)

    if len(values) > 50:
        values.pop(0)

    drawnow(plot_graph)

    time.sleep(0.1)
