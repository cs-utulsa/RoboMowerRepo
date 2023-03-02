import turtle
import PNGtoArray

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

#binary_array = PNGtoArray.image_to_array(doge.png)

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
