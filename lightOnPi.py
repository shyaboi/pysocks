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
    print('all forward!!!')
    forwardBlue()
    forwardRed()

def left():
    print('left hoooooo')
    forwardBlue()
    GPIO.setup(21,GPIO.OUT)
    GPIO.output(21,GPIO.LOW)

def right():
    print('right hoooooo')
    forwardRed()
    GPIO.setup(20,GPIO.OUT)
    GPIO.output(20,GPIO.LOW)

def stop():
    print ("STOP!")
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(21,GPIO.OUT)
    GPIO.output(21,GPIO.LOW)
    GPIO.setup(20,GPIO.OUT)
    GPIO.output(20,GPIO.LOW)

def rev():
    stop()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(26,GPIO.OUT)
    GPIO.output(26,GPIO.HIGH)

