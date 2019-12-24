import time as t
import random as r

print("Welcome to the Math Quiz!")

operator = input("Choose an Operator: ")
minrange = input("Great! Now choose a Minimum for the range: ")
maxrange = input("and the Maximum: ")
print("\nGood! Now I am going to give you five math questions\nwith the operator you put in and in the\nrange you specified.\n")

minrange = (int (minrange))
maxrange = (int (maxrange))
s = 0

if (str (operator)) == "*":
    for i in range(1, 6):
        x = r.randint(minrange, maxrange)
        y = r.randint(minrange, maxrange)

        j =  input("Question " + (str(i)) + "\n" + (str(x)) + "*" + (str(y)) + ": ")
        print((str(x*y)))
        if j == str(x*y):
            print("Correct!\n")
            s = s + 1
        else:
            print("Wrong!\n")

    if s == 5:
        print("\nYou got 'em all correct! Absolutely Outstanding!!")
    elif s == 4:
        print("\nYou got 4/5 correct! Excellent!")
    elif s == 3:
        print("\nYou only got 3/5 correct. Try harder next time.")
    elif s == 0:
        print("\nGo back to Kindergarten right now! You got none correct!!!")
    else:
        print("\nYou only got " + (str(s)) + "/5 correct. Practice those tables will ya?!")
