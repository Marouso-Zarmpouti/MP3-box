"""
buttons.py
Handles all button inputs for the MP3 Player.
Buttons use the ESP32's internal pull-up resistors.
A pressed button reads LOW (False).
"""
from machine import Pin
import config

# Create button objects
play = Pin(config.BTN_PLAY, Pin.IN, Pin.PULL_UP)
next_btn = Pin(config.BTN_NEXT, Pin.IN, Pin.PULL_UP)
prev = Pin(config.BTN_PREV, Pin.IN, Pin.PULL_UP)
menu = Pin(config.BTN_MENU, Pin.IN, Pin.PULL_UP)
power = Pin(config.BTN_POWER, Pin.IN, Pin.PULL_UP)

def play_pressed():
  return play.value() == 0

def next_pressed():
  return next_btn.value() == 0

def prev_pressed():
  return prev.value() == 0

def menu_pressed():
  return menu.value() == 0

def power_pressed():
  return power.value() == 0
