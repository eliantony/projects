from sense_hat import SenseHat
import time
import random

sense = SenseHat()

def smile():
    sense.set_pixel(2, 2, [0, 0, 255])
    sense.set_pixel(4, 2, [0, 0, 255])
    sense.set_pixel(3, 4, [255, 0, 0])
    sense.set_pixel(1, 5, [255, 0, 0])
    sense.set_pixel(2, 6, [255, 0, 0])
    sense.set_pixel(3, 6, [255, 0, 0])
    sense.set_pixel(4, 6, [255, 0, 0])
    sense.set_pixel(5, 5, [255, 0, 0])
    time.sleep(2)
    sense.clear()
    time.sleep(1.5)

def sad():
    sense.set_pixel(2, 2, [0, 0, 255])
    sense.set_pixel(4, 2, [0, 0, 255])
    sense.set_pixel(3, 4, [255, 0, 0])
    sense.set_pixel(1, 7, [255, 0, 0])
    sense.set_pixel(2, 6, [255, 0, 0])
    sense.set_pixel(3, 6, [255, 0, 0])
    sense.set_pixel(4, 6, [255, 0, 0])
    sense.set_pixel(5, 7, [255, 0, 0])
    time.sleep(2)
    sense.clear()
    time.sleep(1.5)

r = random.randint(0, 10)  
l = random.randint(0, 10)
correct = r+l
sense.show_message(str(r) + "+" + str(l) + "=?")
ans = input()
n = int(ans)
if(n == correct):
    smile()
else:
    sad()

