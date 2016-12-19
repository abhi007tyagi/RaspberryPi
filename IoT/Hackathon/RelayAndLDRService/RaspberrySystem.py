import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

lampPin = 18
ldrPin = 17

GPIO.setup(lampPin,GPIO.OUT)
GPIO.setup(ldrPin,GPIO.IN)


def set_lamp_on():
    GPIO.output(lampPin, True)


def set_lamp_off():
    GPIO.output(lampPin, False)


def get_ldr_status():
    if GPIO.input(lampPin):
        print('LAMP-ON')
        reponse = 'LAMP-ON'
    else:
        print('LAMP-OFF')
        response = 'LAMP-OFF'
    return response
