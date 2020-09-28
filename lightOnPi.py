import RPi.GPIO as GPIO
import time

def lightOn():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(21,GPIO.OUT)
    print ("LED on")
    GPIO.output(21,GPIO.HIGH)
def lightOff():
    print ("LED off")
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(21,GPIO.OUT)
    GPIO.output(21,GPIO.LOW)
