import hashlib
from pyfingerprint.pyfingerprint import PyFingerprint
import time
import RPi.GPIO as GPIO


try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)

lock_pin = 18 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(lock_pin,GPIO.OUT)
def unlock():
    print("Unlocking")
    GPIO.output(lock_pin,GPIO.HIGH)             
    time.sleep(3)           
    GPIO.output(lock_pin,GPIO.LOW)
    print("Closed\nPlease scan finger...")


def checkAccess():
    try:
        while( f.readImage() == False):
            pass
        
        f.convertImage(0x01)
    
        result = f.searchTemplate()
    

        positionNumber = result[0]
    
        if (positionNumber == -1 ):
            print'Access denied\nPlease scan finger...'
            return;

        elif (positionNumber == 0):
            print'Access granted'
            unlock()
    
        f.loadTemplate(positionNumber, 0x01)
    
    
    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)

print("Please scan finger...")
try:
    while True:
        if GPIO.input(4) == True:
            checkAccess()
except KeyboardInterrupt : 
    print("\nGoodbye!")
