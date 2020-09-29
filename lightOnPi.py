import RPi.GPIO as GPIO
# import time

# redRev = 26
# red = 20

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)



def forwardRed():
    print ("red team forward")
    GPIO.output(21,GPIO.HIGH)

def forwardBlue():
    print ("blue` team forward")
    GPIO.output(20,GPIO.HIGH)

def forwardAll():
    print('all forward!!!')
    GPIO.output(26,GPIO.LOW)
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
    GPIO.output(20,GPIO.LOW)

def stop():
    print ("STOP!")
    GPIO.setwarnings(False)
    GPIO.output(21,GPIO.LOW)
    GPIO.output(20,GPIO.LOW)
    GPIO.output(26,GPIO.LOW)
    GPIO.output(19,GPIO.LOW)
    

def rev():
    print('reversing...beeep..beep...beep')
    GPIO.output(21,GPIO.LOW)
    GPIO.output(20,GPIO.LOW)
    GPIO.output(26,GPIO.HIGH)
    GPIO.output(19,GPIO.HIGH)

