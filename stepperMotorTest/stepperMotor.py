import RPi.GPIO as GPIO
import time

#pi's pin connect to the ULN2003
IN1 = 10 # GPIO.10
IN2 = 9 # GPIO.9
IN3 = 11 # GPIO.11
IN4 = 8 # GPIO.8

GPIO.setmode(GPIO.BCM)  #use BCM
GPIO.setwarnings(False)

GPIO.setup(IN1, GPIO.OUT)  #Set to output mode
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)


def setStep(h1, h2, h3, h4):
    GPIO.output(IN1, h1)
    GPIO.output(IN2, h2)
    GPIO.output(IN3, h3)
    GPIO.output(IN4, h4)


delay = 0.003  #control speed
steps = 5000  # time

for i in range(0, steps):  # turning clockwise
    setStep(1, 0, 0, 0)
    time.sleep(delay)
    setStep(0, 1, 0, 0)
    time.sleep(delay)
    setStep(0, 0, 1, 0)
    time.sleep(delay)
    setStep(0, 0, 0, 1)
    time.sleep(delay)

setStep(0, 0, 0, 0)
time.sleep(3)
GPIO.cleanup()
