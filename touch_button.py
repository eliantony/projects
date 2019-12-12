import RPi.GPIO as GPIO
import time as t
cappin = 4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(cappin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
while True:
    if GPIO.input(cappin) == True:
        print('You touched the hot lava!')
        t.sleep(1)
        
