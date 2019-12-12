from sense_hat import SenseHat
import time
sense = SenseHat()


def getTemp(): 
    c = sense.get_temperature()
    f = (c*9/5) + 32    
    f = round(f, 0) 
    return int(f)


c = sense.get_temperature()
f = (c*9/5) + 32    
f = round(f, 0) 
msg = "Temperature = %s, " % (f)
print(msg)
sense.show_message(msg, scroll_speed=0.05) 
pf = f
while True:
    if f != pf:
        pf = f
        msg = ("              " + str (f))
        show = str (f)
        print(msg)
        sense.show_message(show, scroll_speed=0.05)
        f = getTemp()
    f = getTemp()
    show = str (f)
    sense.show_message(show, scroll_speed=0.05)
    time.sleep(1)
