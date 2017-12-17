from sense_hat import SenseHat
import time

# KEEP SENSEHAT UPSIDE DOWN

sense = SenseHat()
sense.clear()

g = [0, 255, 0]
r = [255, 0, 0]
e = [0, 0, 0]
s = [255, 170, 0]
p=[
e,e,e,e,g,e,e,e,
e,e,e,g,g,g,e,e,
e,e,g,g,r,g,g,e,
e,e,g,r,g,g,g,e,
e,g,g,g,g,g,g,g,
e,e,e,e,s,e,e,e,
e,e,e,e,s,e,e,e,
e,e,e,e,s,e,e,e
]

def mktree():
    sense.set_pixels(p)
    time.sleep(0.5)
    sense.clear()
    time.sleep(0.5)    
try:    
    while True:
        mktree()    
except KeyboardInterrupt:
    sense.clear()
    pass
    
    

    
