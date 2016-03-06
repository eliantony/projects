from turtle import *


def draw_hexagon():
    for n in range(0,6):
        forward(200)
        right(60)    

def draw_octagon():
    for eli in range(0,8):
        forward(100)
        right(45)
    
shape = input()

if(shape=="1"):
    print ("hexagon")
    draw_hexagon() 

if(shape=="2"):
        print ("octagon")
        draw_octagon()


    
