import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ledPin = 18
ldrPin = 17

GPIO.setup(ledPin,GPIO.OUT)
GPIO.setup(ldrPin,GPIO.IN)


def set_lamp_on():
    GPIO.output(ledPin, True)


def set_lamp_off():
    GPIO.output(ledPin, False)

while True:
    if GPIO.input(ldrPin) == 0:
        set_lamp_on()
    elif GPIO.input(ldrPin) == 1:
        set_lamp_off()
    time.sleep(1)

GPIO.cleanup()
