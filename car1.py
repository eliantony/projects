import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinLineFollower = 25

GPIO.setup(pinLineFollower, GPIO.IN)

try:
    while True:
        GPIO.input(pinLineFollower)==0:
            print("The Sensor is Seeing Black")
        else:
            print("The Sensor is Seeing White")
        time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()

                
