from sense_hat import SenseHat
import time

sense = SenseHat()
sense.set_rotation(180)
sense.show_letter("O",text_colour = [255, 0, 0])
time.sleep(2)
sense.show_letter("M",text_colour = [0, 255, 0])
time.sleep(2)
sense.show_letter("G",text_colour = [0, 0, 255])
time.sleep(2)
sense.show_letter("!",text_colour = [255, 255, 255])
sense.clear()
