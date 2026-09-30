# ============================================================
# CONTROLLING RASPBERRY PI WITH TELEGRAM BOT
# ============================================================
#
# COMMANDS:
#
# Update Raspberry Pi:
# sudo apt update
#
# Install pip:
# sudo apt install python3-pip -y
#
# Install Telegram Library:
# pip3 install telepot
#
# Run Program:
# python3 telegram_control.py
#
#
# TELEGRAM SETUP:
#
# 1. Open Telegram
# 2. Search @BotFather
# 3. Send /start
# 4. Send /newbot
# 5. Create Bot
# 6. Copy Bot Token
#
#
# CONNECTIONS:
#
# LED Positive (+)  ---> Raspberry Pi Pin 11 (GPIO17)
# LED Negative (-)  ---> 220 Ohm Resistor ---> GND Pin 6
#
# ============================================================


import time
import telepot
import RPi.GPIO as GPIO


# LED pin
LED_PIN = 11


# Use Raspberry Pi BOARD pin numbering
GPIO.setmode(GPIO.BOARD)


# Set LED pin as output
GPIO.setup(LED_PIN, GPIO.OUT)


# Turn LED ON
def led_on():

    GPIO.output(LED_PIN, GPIO.HIGH)

    return "LED is ON"


# Turn LED OFF
def led_off():

    GPIO.output(LED_PIN, GPIO.LOW)

    return "LED is OFF"



# Message handling function
def handle(msg):

    chat_id = msg['chat']['id']

    command = msg['text'].lower()


    print("Received command:", command)


    if command == "on":

        response = led_on()

        bot.sendMessage(chat_id, response)


    elif command == "off":

        response = led_off()

        bot.sendMessage(chat_id, response)


    else:

        bot.sendMessage(
            chat_id,
            "Send 'on' to turn LED ON or 'off' to turn LED OFF"
        )



# Replace with your BotFather token
bot = telepot.Bot("YOUR_BOT_TOKEN")


# Start listening
bot.message_loop(handle)


print("Telegram Bot is running...")


try:

    while True:

        time.sleep(10)


except KeyboardInterrupt:

    GPIO.cleanup()
