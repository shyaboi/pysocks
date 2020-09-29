import RPi.GPIO as GPIO
# import time

def forwardRed():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(21,GPIO.OUT)
    print ("red team forward")
    GPIO.output(21,GPIO.HIGH)

def forwardBlue():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(20,GPIO.OUT)
    print ("blue` team forward")
    GPIO.output(20,GPIO.HIGH)

def forwardAll():
    forwardBlue()
    forwardRed()

def left():
    forwardBlue()
    GPIO.setup(21,GPIO.OUT)
    GPIO.output(21,GPIO.LOW)
    
def stop():
    print ("LED off")
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(21,GPIO.OUT)
    GPIO.output(21,GPIO.LOW)
    GPIO.setup(20,GPIO.OUT)
    GPIO.output(20,GPIO.LOW)