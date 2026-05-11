"""
        In this project, an external LED is connected to Pico, and the LED is flashed
    every second.

    Info:
    ****
    Author : Joubair Mohamed Amine.
    Email  : sudo.amine.04@gmail.com

"""
# Import Libraries.
from machine import Pin
from utime import sleep

# Create LED object.
led = Pin(15, Pin.OUT, Pin.PULL_DOWN)

# Main Loop.
while True:
    led.value(1) # Turn ON the LED.
    sleep(1) # Sleep for one second.
    led.value(0) # Turn off the LED.
    sleep(1) # Sleep for one second.

