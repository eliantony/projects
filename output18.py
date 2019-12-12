import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
path = '/home/pi/code/projects/password.txt'
f = open(path, 'r+')
p = f.read().rstrip()
g = [0, 255, 0]
r = [255, 0, 0]
e = [0, 0, 0]
def access(t: str):
    password = p
    if t == password:
        print("You have access")
        GPIO.output(18,GPIO.HIGH)
        time.sleep(3)
        GPIO.output(18,GPIO.LOW)
    elif t == ("##"):
        oldpassword = input("Old Password: ")
        if oldpassword == password:
            password = input("New Password: ")
            print("Password Succesfully Changed")
            g = open(path, 'w')
            g.write(password)
        else:
            print("Sorry Man, Wrong Password\nSee ya later")
    else:
        print("We will flatly say that you simply don't have access.")
access(input("Password(## to change): "))
