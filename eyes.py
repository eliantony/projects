from sense_hat import SenseHat
import time

sense = SenseHat()

w = [150, 150, 150]
b = [0, 0, 255]
e = [0, 0, 0]

p = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
w,w,w,e,e,w,w,w,
w,w,b,e,e,w,w,b,
w,w,w,e,e,w,w,w,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

for x in range (-1, 2):
    sense.set_pixels(p)
    time.sleep(1)
    sense.flip_h()
    time.sleep(1)
    sense.clear()
    time.sleep(2)
