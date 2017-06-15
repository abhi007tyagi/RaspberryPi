import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
motorAPin1 = 21  # pin 40
motorAPin2 = 20  # pin 38

motorBPin1 = 24  # pin 18
motorBPin2 = 23  # pin 16

GPIO.setup(motorAPin1, GPIO.OUT)
GPIO.setup(motorAPin2, GPIO.OUT)
GPIO.setup(motorBPin1, GPIO.OUT)
GPIO.setup(motorBPin2, GPIO.OUT)


def on_control(action):
    print("Action received: " + action)
    if str(action) == "FW'":
        GPIO.output(motorAPin1, True)
        GPIO.output(motorAPin2, False)
        GPIO.output(motorBPin1, False)
        GPIO.output(motorBPin2, True)
        print("Move Forward")
    elif str(action) == "BW'":
        GPIO.output(motorAPin1, False)
        GPIO.output(motorAPin2, True)
        GPIO.output(motorBPin1, True)
        GPIO.output(motorBPin2, False)
        print("Move Backward")
    elif str(action) == "LT'":
        GPIO.output(motorAPin1, True)
        GPIO.output(motorAPin2, False)
        GPIO.output(motorBPin1, False)
        GPIO.output(motorBPin2, False)
        print("Move Left")
    elif str(action) == "RT'":
        GPIO.output(motorAPin1, False)
        GPIO.output(motorAPin2, False)
        GPIO.output(motorBPin1, False)
        GPIO.output(motorBPin2, True)
        print("Move Right")
    elif str(action) == "ST'":
        GPIO.output(motorAPin1, False)
        GPIO.output(motorAPin2, False)
        GPIO.output(motorBPin1, False)
        GPIO.output(motorBPin2, False)
        print("Stop Moving")
    else:
        print("Action not supported!!")


GPIO.cleanup()


