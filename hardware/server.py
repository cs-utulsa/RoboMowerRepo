


class ServerSocketCar(object):
server.py
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
