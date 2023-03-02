import RPi.GPIO as GPIO
import time
import turtle
import Draw


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

# Define the movements to draw the pattern
def onecycle():
    forward()
    for i in range(69):
        time.sleep(0.01)
        forward()

    stop()


def zigzag():
    for i in range(29):
        onecycle()
        if i % 2 == 0:
            if i != 28:
                left()
                time.sleep(0.2)
                stop()
                right()
                time.sleep(0.2)
                stop()
        else:
            right()
            time.sleep(0.2)
            stop()
            left()
            time.sleep(0.2)
            stop()


binary_array = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

numrows = len(binary_array)
numcols = len(binary_array[0])

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

def onecycle():
    global rows
    for i in range(numcols):
        if binary_array[rows][i] == 1:
            a.pendown()
            a.forward(10)
        else:
            a.penup()
            a.forward(10)
    rows += 1

for i in range(numrows):
    onecycle()
    if rows % 2 == 1:
        a.right(90)
        a.penup()
        a.forward(10)
        a.right(90)
    else:
        a.left(90)
        a.penup()
        a.forward(10)
        a.left(90)

turtle.exitonclick()


'''

# Initialize the turtle graphics window
binary_array = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

numrows = len(binary_array)
numcols = len(binary_array[0])

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
def turtle_to_robot_forward():
    forward()
    a.forward(10)

def turtle_to_robot_left():
    left()
    a.left(90)

def turtle_to_robot_right():
    right()
    a.right(90)

def onecycle():
    global rows
    for i in range(numcols):
        if binary_array[rows][i] == 1:
            a.pendown()
            turtle_to_robot_forward()
        else:
            a.penup()
            turtle_to_robot_forward()
    rows += 1

# Call the turtle commands and convert them to robot movements
for i in range(numrows):
    onecycle()
    if rows % 2 == 0:
        turtle_to_robot_left()
        a.penup()
        turtle_to_robot_forward()
        turtle_to_robot_left()
    else:
        turtle_to_robot_right()
        a.penup()
        turtle_to_robot_forward()
        turtle_to_robot_right()
'''
