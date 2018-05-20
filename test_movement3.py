"""
Tests for minibot movement.
"""
from minibot.bot import Bot

import json

CONFIG_LOCATION = '/home/pi/cs-minibot/minibot/configs/config.json'

p=75

if __name__ == "__main__":
    print("Initializing Minibot Software")
    config_file = open(CONFIG_LOCATION)
    config = json.loads(config_file.read())
    bot = Bot(config)
    print("Moving Forward - 3 seconds")
    bot.move_forward(p)
    bot.wait(3)
    print("Moving Backward - 3 seconds")
    bot.move_backward(p)
    bot.wait(3)
    print("Turning Left - 3 seconds")
    bot.turn_counter_clockwise(p)
    bot.wait(3)
    print("Turning Right - 3 seconds")
    bot.turn_clockwise(p)
    bot.wait(3)
    print("Stop")
    bot.stop()
