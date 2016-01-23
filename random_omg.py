from sense_hat import SenseHat
import time
import random 

sense = SenseHat()

sense.set_rotation(180)
r = random.randint (0, 255)
sense.show_letter("O",text_colour = [0, r, r])
time.sleep(2)

r = random.randint(0, 255)
sense.show_letter("M",text_colour = [r, r, 0])
time.sleep(2)

r = random.randint(0, 255)
sense.show_letter("G",text_colour = [r, r, 0])
time.sleep(2)

r = random.randint(0, 255)
sense.show_letter("!",text_colour = [0, r, r])
time.sleep(1)
sense.clear()
