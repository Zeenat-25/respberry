# Controlling Raspberry Pi with Telegram Bot
#
# Commands:
# git clone https://github.com/Zeenat-25/respberry.git
# cd respberry
# sudo apt update
# sudo apt install python3-pip -y
# pip3 install telepot
#github.com/salmanfarissvp/TelegramBot.git
# python3 telegram_control.py
#
# Telegram:
# 1. Open Telegram
# 2. Search @BotFather
# 3. Send /start
# 4. Send /newbot
# 5. Create the bot
# 6. Copy the Bot Token
#
# Connections:
# LED Positive (+) -> Pin 11 (GPIO17)
# LED Negative (-) -> 220 Ohm Resistor -> GND Pin 6

import time
import telepot
import RPi.GPIO as GPIO

LED_PIN = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)


def led_on():
    GPIO.output(LED_PIN, GPIO.HIGH)
    return "LED is ON"


def led_off():
    GPIO.output(LED_PIN, GPIO.LOW)
    return "LED is OFF"


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text'].lower()

    print("Received command:", command)

    if command == "on":
        bot.sendMessage(chat_id, led_on())

    elif command == "off":
        bot.sendMessage(chat_id, led_off())

    else:
        bot.sendMessage(chat_id, "Send 'on' or 'off'")


bot = telepot.Bot("SALMAN_BOT_TOKEN")

bot.message_loop(handle)

print("Telegram Bot is running...")

try:
    while True:
        time.sleep(10)

except KeyboardInterrupt:
    GPIO.cleanup()
