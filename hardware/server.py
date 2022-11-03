PhoNoodles
#2579

PhoNoodles — Today at 10:21 PM
again this is just the first prototype for this project
so we can use this code for the next one
pins are 22, 23, 24, and 25 correct?
ShleyMeister — Today at 10:29 PM
yup
PhoNoodles — Today at 10:40 PM
#import modules
import sys
import pygame
from pygame.locals import *
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
Expand
RoboPrototype.py
3 KB
see if that works
typed as fast as i can
because the thing cant be copy and paste
fingers crossed
if this work, i can start synchronizing this code with the library that xingzhou provided
ShleyMeister — Today at 11:00 PM
i dont think the input from my keyboard will do it, maybe its expecting a keyboard input from the raspberry pi? I tried using a dongle but i got nothing. I even looked over and fixed a part of it but i got nothing
PhoNoodles — Today at 11:05 PM
Do you think it might be the raspberry pi?
Also are you doing arrow keys or wasd
ShleyMeister — Today at 11:07 PM
wasd but not gonna lie i tried both
PhoNoodles — Today at 11:08 PM
that is so weird
everything is followed accordingly
it must have to do something with the raspberry pi
ShleyMeister — Today at 11:09 PM
yeah im at a loss as well at whats wrong. maybe. Its running on the raspberry pi, but maybe theres an issue with the pins?
PhoNoodles — Today at 11:10 PM
because you said the same thing was happening to the one xingzhou put right?
then there must be something up with the raspberry pi i think
guess best is to look through the document and see if there is any differnces
ShleyMeister — Today at 11:10 PM
yeah but your pins were right in the code, im more saying maybe there's something wrong with the pins on the rasp pi
PhoNoodles — Today at 11:11 PM
ohhh
ShleyMeister — Today at 11:11 PM
i did, i fixed a problem and it let the program run indefinitely, but not running :/
PhoNoodles — Today at 11:12 PM
so is the client working?
but the instructions is not working for the raspberry pi
ShleyMeister — Today at 11:15 PM
yup
PhoNoodles — Today at 11:16 PM
this is a stupid question but we know that the motor power are on right
or as i say it wired correctly
right now i think there might be something up with the robot because we know the client works and the server works
its must be something with the robot
ShleyMeister — Today at 11:17 PM
yes. the card has a red led to let me know its powered
PhoNoodles — Today at 11:17 PM
hmm
ShleyMeister — Today at 11:18 PM
yeah, ive triple checked which wires went where
PhoNoodles — Today at 11:18 PM
that is so weird what the heck
i could take it to riley rq
meet him early in the morning and see if he can help us
before presenting it
ShleyMeister — Today at 11:19 PM
sure, id be down. I have class at 11 but i can meet before then
PhoNoodles — Today at 11:19 PM
because worst comes to worst, riley has his built and we can just use that lol
i am down
im just gonna keep looking at this
just lmk if you get a breakthrough
but i think the code that xingzhou is working
because the code that we used is from youngwoks and if that isnt working then it must be a hardware issue
ShleyMeister — Today at 11:21 PM
yeah im leaning towards a hardware issue too. a part must be malfunctioning or something
PhoNoodles — Today at 11:21 PM
might have to use riley to start just for now if we cant figure it out when we meet up with him
so are we gonna assume that the code that xingzhou provided works?
also can send me the code for both the clience and the server so i can edit it
ShleyMeister — Today at 11:23 PM
import pygame
import socket
import sys


class ClientSocketCar(object):
Expand
clience.py
5 KB
import RPi.GPIO as GPIO
import socket
import time


class ServerSocketCar(object):
Expand
server.py
4 KB
﻿
import RPi.GPIO as GPIO
import socket
import time


class ServerSocketCar(object):
    '''
    create socket
    '''
    def __init__(self):

        self.car_pi = CarPi()
        # create server socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(('', 9900))
        self.server_socket.listen(128)

    def recv_socket(self):
        # link successfully, going back to the socket
        self.client_socket, self.port_ip = self.server_socket.accept()
        # print current clint
        print('link successfully, current clint is: ', self.port_ip)
        # recieve and send data
        while True:
            # reciedve data, and decoding
            self.date = self.client_socket.recv(1024)
            self.recv_data = self.date.decode('utf-8')
            # When data is empty, that means disconnect, it's over, next clint
            if not self.recv_data:
                print('link disconnect--bye')
                # set duty cycle to 50%
                self.car_pi.dc = 50
                return
            # hardware operation
            self.car_pi.car_way(self.recv_data)

    def main_run(self):
        '''
        programing running entry
        '''
        while True:
            self.recv_socket()

    def __del__(self):
        '''
        collect resources
        '''
        self.client_socket.close()
        self.server_socket.close()


class CarPi(object):
    '''
    create raspberry
    '''
    # initializing hardware
    def __init__(self):
        # initializing pin
        GPIO.setmode(GPIO.BCM)  # set pinmode
        GPIO.setwarnings(False)  # Ignore pin setting error report error when pin is not 'IN' status
        # # my GPIO [4, 17, 10 ,9, 11, 14, 15 ,18 ,22, 23 ,24, 25, 8, 7]
        # # two software pwm, two direction interface
        GPIO.setup((22, 23, 24, 25), GPIO.OUT) # the pin that going to be used (22,23,24,25)
        self.pin_p1 = GPIO.PWM(22, 23)
        self.pin_p2 = GPIO.PWM(24, 25)
        # duty cycle
        self.dc = 50
        self.pin_p1.start(self.dc)
        self.pin_p2.start(self.dc)

    def car_way(self, way):
        '''
        Change the running state of the mower
        '''

        # duty cycle must be 0-100, otherwise end automatically
        if way == 'up' and 0 <= self.dc < 100:
            self.dc += 3
            self.pin_p1.ChangeDutyCycle(self.dc)
            self.pin_p2.ChangeDutyCycle(self.dc)
            # print('speed+1', self.dc)
        if way == 'down' and 0 < self.dc <= 100:
            self.dc -= 3
            self.pin_p1.ChangeDutyCycle(self.dc)
            self.pin_p2.ChangeDutyCycle(self.dc)
            # print('speed-1', self.dc)
        if way == 'left':
            GPIO.setup((10, 9), GPIO.OUT)
            GPIO.output(10, GPIO.LOW)
            GPIO.output(9, GPIO.HIGH)
            GPIO.cleanup((10, 9))
            # print('turning left+1')
        if way == 'right':
            GPIO.setup((10, 9), GPIO.OUT)
            GPIO.output(10, GPIO.HIGH)
            GPIO.output(9, GPIO.LOW)
            GPIO.cleanup((10, 9))
            # print('turning right-1')

        def __del__(self):
            '''
            clena up the port after running the program
            '''
            GPIO.cleanup()

        if __name__ == '__main__':
            car = ServerSocketCar()
            car.main_run()
