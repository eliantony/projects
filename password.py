import time 
from sense_hat import SenseHat
sense = SenseHat()
path = '/home/pi/code/projects/password.txt'
f = open(path, 'r+')
p = f.read().rstrip()
g = [0, 255, 0] 
r = [255, 0, 0]
e = [0, 0, 0]
check = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,g,e,
e,e,e,e,e,g,e,e,
e,e,g,e,g,e,e,e,
e,e,e,g,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
]
cross = [
e,e,e,e,e,e,e,e,
e,e,r,e,e,e,r,e,
e,e,e,r,e,r,e,e,
e,e,e,e,r,e,e,e,
e,e,e,r,e,r,e,e,
e,e,r,e,e,e,r,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
]
def access(t: str):
    password = p
    if t == password:
        print("You have access")
        sense.show_message(t)
        sense.set_pixels(check)
        time.sleep(3)
        sense.clear()
    elif t == ("##"):
        oldpassword = input("Old Password: ")
        if oldpassword == password:
            password = input("New Password: ")
            print("Password Succesfully Changed")
            sense.show_message("New Password: " + password)
            sense.set_pixels(check)
            time.sleep(3)
            sense.clear()
            g = open(path, 'w')
            g.write(password)
        else:
            print("Sorry Man, Wrong Password\nSee ya later")
            sense.set_pixels(cross)
            time.sleep(3)
            sense.clear()
    else:
        print("We will flatly say that you simply don't have access.")
        sense.show_message(t)
        sense.set_pixels(cross)
        time.sleep(3)
        sense.clear()
access(input("Password(## to change): "))        

