import RPi.GPIO as GPIO
# import time

def lightOnA():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(21,GPIO.OUT)
    print ("LED on")
    GPIO.output(21,GPIO.HIGH)
def lightOnS():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(20,GPIO.OUT)
    print ("LED on")
    GPIO.output(20,GPIO.HIGH)
def lightOff():
    print ("LED off")
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(21,GPIO.OUT)
    GPIO.output(21,GPIO.LOW)
    GPIO.setup(20,GPIO.OUT)
    GPIO.output(20,GPIO.LOW)