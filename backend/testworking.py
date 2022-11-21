import time

from gpiozero import Robot
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory(host='192.168.1.32') #change ip to what the ip is for the RoboMower

robot = Robot(left=(23, 22), right=(24, 25), pin_factory=factory)


#runs the robot forward at max speed 1 for 1 second
robot.forward(1)
time.sleep(1)
#runs the robot backwards at max speed 1 for 1 second
robot.backward(1)
time.sleep(1)
robot.stop()