#!/usr/bin/env python3
#Name: light.py
#Purpose: Class which controls various LED functions. 
#Developer: Jonathan Coffey

from keyboard import Keyboard
from os import error
from gpiozero import RGBLED
from colorzero import Color
from time import sleep

class Light:

    # param in order: Red, Green, Blue
    def __init__(self, pin1, pin2, pin3):
        self.led = RGBLED(pin1, pin2, pin3)

    def onWithDelay(self, colStr, delay):
        if (delay > 0):
            self.led.color = Color(colStr)
            sleep(delay)
            self.turnOff()
        elif (delay == 0):
            self.led.color = Color(colStr)
        else:
            print(f'Invalid delay of {delay} seconds')

    # Default color will be white
    def turnOn(self, color='white'):
        self.led.color = Color(color)

    def turnOff(self):
        self.led.off()

    # Flashes the light of the selected color 3 times
    def flash(self, colstr):
        for i in range(3):
            self.led.color = Color(colstr)
            sleep(0.1)
            self.turnOff()
            sleep(0.1)

    def flashLearningMode(self):
        for i in range(2):
            for key in Keyboard.KEY_COLORS:
                self.led.color = Color(Keyboard.KEY_COLORS.get(key))
                sleep(0.1)
                self.turnOff()
            sleep(0.2)
