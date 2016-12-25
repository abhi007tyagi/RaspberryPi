import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

motorPin = 18
btnPin = 17

GPIO.setup(motorPin, GPIO.OUT)
GPIO.setup(btnPin, GPIO.IN)


def start_motor():
    if GPIO.input(motorPin) == 0:
        GPIO.output(motorPin, True)
        print('motor started')


def stop_motor():
    if GPIO.input(motorPin) == 1:
        GPIO.output(motorPin, False)
        print('motor stopped')


while True:
    if GPIO.input(btnPin) == 0:
        start_motor()
    elif GPIO.input(btnPin) == 1:
        stop_motor()

GPIO.cleanup()
