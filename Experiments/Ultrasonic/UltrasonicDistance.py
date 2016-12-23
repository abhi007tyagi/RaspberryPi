import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
# Define GPIO to use on Pi
TRIG = 23
ECHO = 24

print("Ultrasonic Measurement")

# Set pins as output and input
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

for i in range(1, 50):
    # Set trigger to False (Low)
    GPIO.output(TRIG, False)

    # Allow module to settle
    time.sleep(0.1)
    # Send 10us pulse to trigger
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    start = time.time()
    while GPIO.input(ECHO) == 0:
        start = time.time()
    while GPIO.input(ECHO) == 1:
        stop = time.time()

    # Calculate pulse length
    elapsed = stop - start
    # Distance pulse travelled in that time is time
    # multiplied by the speed of sound (cm/s)
    distance = elapsed * 17000
    print("Distance : %.1f cm" % distance)

    time.sleep(0.5)

# Reset GPIO settings
GPIO.cleanup()
