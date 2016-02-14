import RPi.GPIO as GPIO
import random
import time


# left_name = input('Left Players Name Is:')
# right_name = input("Right Player's Name Is")

# names = [left_name, right_name]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 4
right_button = 15
left_button = 14

GPIO.setup(led, GPIO.OUT)
GPIO.setup(right_button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(left_button, GPIO.IN, GPIO.PUD_UP)


GPIO.output(led, 1)
time.sleep(random.uniform (5, 15))
GPIO.output(led, 0)


while True:
    if GPIO.input(left_button) == False:
       print('Left Button Pressed')
       break
    if GPIO.input(right_button) == False:
        print('Right Button pressed')
        break

GPIO.cleanup()

