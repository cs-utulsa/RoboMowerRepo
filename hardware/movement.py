import turtle
import PNGtoArray
import serial
import time
import keyboard


# Set up serial communication
print("Program starting...")
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
# Delay for the Arduino to initialize
time.sleep(2)
print("Connection established!")

binary_array = PNGtoArray.image_to_array(doge.png)

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
bool = True

rows = 0


def moveForwardOrBackward(bool):
    if bool == True:
        ser.write(bytes([0x01]))
    else:
        ser.write(bytes([0x02]))


def movePenUpOrDown(bool):
    if bool == True:
        ser.write(bytes([0x10]))
    else:
        ser.write(bytes([0x20]))


def onecycle():
    global rows
    for i in range(numcols):
        if binary_array[rows][i] == 1:
            moveLightOnOrOff(True)
            moveForwardOrBackward(bool)
            time.sleep(0.1)
        else:
            moveLightOnOrOff(False)
            moveForwardOrBackward(bool)
            time.sleep(0.1)
    rows += 1


for i in range(numrows):
    onecycle()
    if rows % 2 == 1:
        ser.write(bytes([0x04]))
        time.sleep(0.1)
        moveLightOnOrOff(False)
        moveForwardOrBackward(bool)
        time.sleep(0.1)
        ser.write(bytes([0x04]))
        time.sleep(0.1)
    else:
        ser.write(bytes([0x03]))
        time.sleep(0.1)
        moveLightOnOrOff(False)
        moveForwardOrBackward(bool)
        time.sleep(0.1)
        ser.write(bytes([0x03]))
        time.sleep(0.1)
    if (bool == True):
        bool = False
    else:
        bool = True

turtle.exitonclick()
