import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt


GPIO.setmode(GPIO.BCM)
ledPin = 18
GPIO.setup(ledPin, GPIO.OUT)


# This is the Subscriber
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("topic/led")


def on_message(client, userdata, msg):
    print("Message received: " + str(msg.payload))
    if str(msg.payload) == "b'ON'":
        print("LED ON")
        GPIO.output(ledPin, True)
        # client.disconnect()
    elif str(msg.payload) == "b'OFF'":
        print("LED OFF")
        GPIO.output(ledPin, False)
        # client.disconnect()
    else:
        print("Message not supported!!")
        # client.disconnect()


client = mqtt.Client()
client.connect("127.0.0.1", 1883, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()

GPIO.cleanup()


