#import modules
import sys
import pygame
from pygame.locals import *
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pygame.init()

# pygame screen
SCREEN_SIZE = (500, 500)
screen = pygame.display.set_mode((SCREEN_SIZE))
pygame.display.set_caption('Raspberry Pi RoboMower Prototype #1')

# pin configuration
# left wheel
left_wheel_pin1 = 22
left_wheel_pin2 = 23
# right_wheel
right_wheel_pin3 = 24
right_wheel_pin4 = 25

# pin setup
GPIO.setup([left_wheel_pin1, left_wheel_pin2,
           right_wheel_pin3, right_wheel_pin4])

# direction variables
foward = False
reverse = False
turn_left = False
turn_right = False

# pygame main loop
while True:

    # event checker
    for event in pygame.event.get():

        # window close event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:

            # foward
            if event.key == K_w:
                foward = True
            if event.key == K_s:
                reverse = True
            if event.key == K_a:
                turn_left = True
            if event.key == K_d:
                turn_right = True

        if event.type == KEYUP:
            foward = reverse = turn_left = turn_right = False
            GPIO.output([left_wheel_pin1, left_wheel_pin2,
                        right_wheel_pin3, right_wheel_pin4], GPIO.LOW)

    if foward:
        GPIO.output([left_wheel_pin1, right_wheel_pin4], GPIO.LOW)
        GPIO.output([left_wheel_pin2, right_wheel_pin3], GPIO.HIGH)

    if reverse:
        GPIO.output([left_wheel_pin1, right_wheel_pin4], GPIO.HIGH)
        GPIO.output([left_wheel_pin2, right_wheel_pin3], GPIO.LOW)

    if turn_left:
        GPIO.output([left_wheel_pin1, left_wheel_pin2,
                    right_wheel_pin4], GPIO.LOW)
        GPIO.output([right_wheel_pin3], GPIO.HIGH)

    if turn_right:
        GPIO.output([left_wheel_pin1, right_wheel_pin3,
                    right_wheel_pin4], GPIO.LOW)
        GPIO.output([left_wheel_pin2], GPIO.HIGH)

    # update screen
    pygame.display.update()
