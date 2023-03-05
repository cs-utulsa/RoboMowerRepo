import RPi.GPIO as GPIO
import time
import PNGtoArray
import turtle

# Define the pins connected to the left motor
left_motor_forward_pin = 11
left_motor_backward_pin = 12

# Define the pins connected to the right motor
right_motor_forward_pin = 15
right_motor_backward_pin = 16

# Initialize the GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(left_motor_forward_pin, GPIO.OUT)
GPIO.setup(left_motor_backward_pin, GPIO.OUT)
GPIO.setup(right_motor_forward_pin, GPIO.OUT)
GPIO.setup(right_motor_backward_pin, GPIO.OUT)

# Defining the pins for mower on and off by using LED method
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

ledPin = 12

GPIO.setup(ledPin, GPIO.OUT)

# Define the robot's movements
def forward():
    GPIO.output(left_motor_forward_pin, GPIO.HIGH)
    GPIO.output(right_motor_forward_pin, GPIO.HIGH)
    GPIO.output(left_motor_backward_pin, GPIO.LOW)
    GPIO.output(right_motor_backward_pin, GPIO.LOW)


def backward():
    GPIO.output(left_motor_forward_pin, GPIO.LOW)
    GPIO.output(right_motor_forward_pin, GPIO.LOW)
    GPIO.output(left_motor_backward_pin, GPIO.HIGH)
    GPIO.output(right_motor_backward_pin, GPIO.HIGH)


def left():
    GPIO.output(left_motor_forward_pin, GPIO.LOW)
    GPIO.output(right_motor_forward_pin, GPIO.HIGH)
    GPIO.output(left_motor_backward_pin, GPIO.HIGH)
    GPIO.output(right_motor_backward_pin, GPIO.LOW)


def right():
    GPIO.output(left_motor_forward_pin, GPIO.HIGH)
    GPIO.output(right_motor_forward_pin, GPIO.LOW)
    GPIO.output(left_motor_backward_pin, GPIO.LOW)
    GPIO.output(right_motor_backward_pin, GPIO.HIGH)


def stop():
    GPIO.output(left_motor_forward_pin, GPIO.LOW)
    GPIO.output(right_motor_forward_pin, GPIO.LOW)
    GPIO.output(left_motor_backward_pin, GPIO.LOW)
    GPIO.output(right_motor_backward_pin, GPIO.LOW)

def down():
    GPIO.output(ledPin, GPIO.HIGH)


def up():
    GPIO.output(ledPin, GPIO.LOW)


binaryArt = PNGtoArray.image_to_array()
# Initialize the turtle graphics window
numrows = len(binaryArt)
numcols = len(binaryArt[0])

screen_width = numcols * 10
screen_height = numrows * 10

turtle.setup(width=screen_width, height=screen_height)
turtle.bgcolor("white")

a = turtle.Turtle()
a.penup()
a.goto(-screen_width/2, screen_height/2)
a.pendown()
a.speed(10)
a.pensize(3)
a.color("green")

rows = 0

# Convert the turtle commands to robot movements
def turtle_to_robot_forward(distance):
    forward()
    a.forward(distance)

def turtle_to_robot_left(angle):
    left()
    a.left(angle)

def turtle_to_robot_right(angle):
    right()
    a.right(angle)

def turtle_to_robot_pendown():
    down()
    a.pendown()

def turtle_to_robot_penup():
    up()
    a.penup()

# Define the movements to draw the pattern
def onecycle():
    global rows
    for i in range(numcols):
        if binaryArt[rows][i] == 1:
            turtle_to_robot_pendown()
            turtle_to_robot_forward(10)
        else:
            turtle_to_robot_penup()
            turtle_to_robot_forward(10)
    rows += 1

for i in range(numrows):
    onecycle()
    if rows % 2 == 1:
        turtle_to_robot_right(90)
        turtle_to_robot_penup()
        turtle_to_robot_forward(10)
        turtle_to_robot_right(90)
    else:
        turtle_to_robot_left(90)
        turtle_to_robot_penup()
        turtle_to_robot_forward(10)
        turtle_to_robot_left(90)
