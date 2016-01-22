from sense_hat import SenseHat
sense = SenseHat()
#for x in range (10,-1,-1):
#     sense.show_message(str(x) + "!")   
#sense.show_message("10! 9! 8! 7! 
sense.set_rotation(180)
red = (255, 0, 0)
green = (0,255,0)
blue =(0, 0, 255)
for i in range(1,11):
	sense.show_message("Antony family",scroll_speed = 0.05,text_colour = blue, back_colour = red)
	sense.show_message(str(i), text_colour = blue )
sense.clear()
