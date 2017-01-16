import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ledPin = 18
pirPin = 17

GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(pirPin, GPIO.IN)


def set_lamp_on():
    GPIO.output(ledPin, True)


def set_lamp_off():
    GPIO.output(ledPin, False)


while True:
    if GPIO.input(pirPin) == 0:
        print("low")
        set_lamp_off()
    elif GPIO.input(pirPin) == 1:
        print("high")
        set_lamp_on()
    time.sleep(1)

GPIO.cleanup()
