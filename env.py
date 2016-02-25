from sense_hat import SenseHat
import time
sense = SenseHat()


while True:
    t = sense.get_temperature()
    
    t = round(t, 1)
 
    msg = "Tempreture = %s, " % (t)
    print(msg)
    sense.show_message(msg, scroll_speed=0.05)

    time.sleep(1.5)
