# ============================================================
# RASPBERRY PI BASED OSCILLOSCOPE
# ============================================================
#
# GITHUB COMMANDS:
#
# Clone Repository:
# git clone https://github.com/Zeenat-25/respberry.git
#
# Go inside repository:
# cd respberry
#
# Install required packages:
# sudo apt update
# sudo apt install python3-dev python3-smbus python3-matplotlib git -y
#
# Install ADS1115 Library:
# git clone https://github.com/adafruit/Adafruit_Python_ADS1x15.git
# cd Adafruit_Python_ADS1x15
# sudo python3 setup.py install
# cd ..
#
# Install plotting library:
# pip3 install drawnow --break-system-packages
#
# Run Program:
# python3 oscilloscope.py
#
#
# ============================================================
# HARDWARE CONNECTIONS:
# ============================================================
#
# ADS1115          Raspberry Pi
# --------------------------------
# VCC       --->    Physical Pin 17 (3.3V)
# GND       --->    Physical Pin 6 (GND)
# SDA       --->    Physical Pin 3 (GPIO 2 - SDA)
# SCL       --->    Physical Pin 5 (GPIO 3 - SCL)
#
# Analog Signal:
# Signal    --->    ADS1115 A0
# Ground    --->    ADS1115 GND
#
# ============================================================


import time
import matplotlib.pyplot as plt
from drawnow import drawnow
import Adafruit_ADS1x15


# Create ADS1115 ADC object
adc = Adafruit_ADS1x15.ADS1115()


# Gain setting
GAIN = 1


# Store ADC values
values = []


# Setup graph
plt.ion()


# Function to update graph
def plot_graph():

    plt.title("Raspberry Pi Based Oscilloscope")
    plt.xlabel("Time")
    plt.ylabel("ADC Value")

    plt.grid(True)

    plt.plot(values)



# Main Program
print("Oscilloscope Started...")
print("Reading ADS1115 Channel 0")


while True:

    # Read analog value from A0 channel
    adc_value = adc.read_adc(0, gain=GAIN)


    print("ADC Value:", adc_value)


    # Store value
    values.append(adc_value)


    # Maintain last 50 readings
    if len(values) > 50:
        values.pop(0)


    # Update graph
    drawnow(plot_graph)


    # Delay
    time.sleep(0.1)
