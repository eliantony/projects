import time
from sense_hat import SenseHat
sense = SenseHat()

speed = 0.05
sense.show_message("Knock Knock", scroll_speed = speed)
time.sleep(2)
sense.show_message("Kertich!" , scroll_speed = speed)
time.sleep(2)
sense.show_message("God Bless you!!" , scroll_speed = speed)

time.sleep(2)
sense.clear()
