from sense_hat import SenseHat
import time
sense = SenseHat()
sense.gamma_reset()
#for x in range (10,-1,-1):
#     sense.show_message(str(x) + "!")   
#sense.show_message("10! 9! 8! 7! 
sense.set_rotation(180)
red = (255, 111, 14)
black = (0, 0 ,0)



def loop():
        while True:
            sense.show_message("KONBANHA SHI MASU!!",scroll_speed = 0.175,text_colour = black, back_colour = red)
           # sense.show_message(str(i), text_colour = blue)   

try:
        loop()
except KeyboardInterrupt:
        sense.clear()
       
