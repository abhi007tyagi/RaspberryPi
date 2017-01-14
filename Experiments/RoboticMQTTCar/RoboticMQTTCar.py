import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt


GPIO.setmode(GPIO.BCM)
motorAPin1 = 21  # pin 40
motorAPin2 = 20  # pin 38

motorBPin1 = 24  # pin 18
motorBPin2 = 23  # pin 16

GPIO.setup(motorAPin1, GPIO.OUT)
GPIO.setup(motorAPin2, GPIO.OUT)
GPIO.setup(motorBPin1, GPIO.OUT)
GPIO.setup(motorBPin2, GPIO.OUT)


# This is the Subscriber
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("topic/led")


def on_message(client, userdata, msg):
    print("Message received: " + str(msg.payload))
    if str(msg.payload) == "b'FW'":
        GPIO.output(motorAPin1, True)
        GPIO.output(motorAPin2, False)
        GPIO.output(motorBPin1, False)
        GPIO.output(motorBPin2, True)
        print("Move Forward")
    elif str(msg.payload) == "b'BW'":
        GPIO.output(motorAPin1, False)
        GPIO.output(motorAPin2, True)
        GPIO.output(motorBPin1, True)
        GPIO.output(motorBPin2, False)
        print("Move Backward")
    elif str(msg.payload) == "b'LT'":
        GPIO.output(motorAPin1, True)
        GPIO.output(motorAPin2, False)
        GPIO.output(motorBPin1, False)
        GPIO.output(motorBPin2, False)
        print("Move Left")
    elif str(msg.payload) == "b'RT'":
        GPIO.output(motorAPin1, False)
        GPIO.output(motorAPin2, False)
        GPIO.output(motorBPin1, False)
        GPIO.output(motorBPin2, True)
        print("Move Right")
    elif str(msg.payload) == "b'ST'":
        GPIO.output(motorAPin1, False)
        GPIO.output(motorAPin2, False)
        GPIO.output(motorBPin1, False)
        GPIO.output(motorBPin2, False)
        print("Stop Moving")
    else:
        print("Message not supported!!")
        # client.disconnect()


client = mqtt.Client()
client.connect("127.0.0.1", 1883, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()

GPIO.cleanup()


