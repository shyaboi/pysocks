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
    GPIO.output(26,GPIO.LOW)
    forwardBlue()
    GPIO.setup(21,GPIO.OUT)
    GPIO.output(21,GPIO.LOW)

def right():
    GPIO.output(26,GPIO.LOW)
    print('right hoooooo')
    forwardRed()
    GPIO.setup(20,GPIO.OUT)
    GPIO.output(20,GPIO.LOW)

def stop():
    print ("STOP!")
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(21,GPIO.OUT)
    GPIO.setup(20,GPIO.OUT)
    GPIO.setup(26,GPIO.OUT)
    GPIO.output(21,GPIO.LOW)
    GPIO.output(20,GPIO.LOW)
    GPIO.output(26,GPIO.LOW)

def rev():
    print('reversing...beeep..beep...beep')
    GPIO.output(21,GPIO.LOW)
    GPIO.output(20,GPIO.LOW)
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(26,GPIO.OUT)
    GPIO.output(26,GPIO.HIGH)

