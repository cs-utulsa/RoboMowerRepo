import pygame
import socket
import sys


class ClientSocketCar(object):
    '''
    Network socket, used for sending data
    '''
    def __init__(self):
        '''
        initializing network socket
        '''
        self.clinet_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create Network socket
        self.clinet_socket.connect(('172.16.194.57', 9900))  # ip address ,port number

    # sending data
    def up_socket(self):
        self.clinet_socket.send('up'.encode('utf-8'))

    def down_socket(self):
        self.clinet_socket.send('down'.encode('utf-8'))

    def left_socket(self):
        self.clinet_socket.send('left'.encode('utf-8'))

    def right_socket(self):
        self.clinet_socket.send('right'.encode('utf-8'))

    def __del__(self):
        self.clinet_socket.close()


class Point(object):
    '''
    create button
    '''
    # initializing
    def __init__(self):
        # socket target
        self.car_socket = ClientSocketCar()
        # loading image
        self.image_point1 = pygame.image.load('point_vert.png')  # IMAGE1
        self.image_point2 = pygame.image.load('point_horiz.png')  # IMAGE2
        # convert image to rectangle
        self.img_rect1 = self.image_point1.get_rect()  # rectangle1 centerx=100, centery=130
        self.img_rect2 = self.image_point2.get_rect()  # rectangle2 centerx=390, centery=130
        self.img_rect1.move_ip(100, 130)
        self.img_rect2.move_ip(390, 130)
        # button speed
        self.speed = 8

    def move_left(self):
        '''
        left
        '''
        # Determine the x-direction position of the rectangle object
        if self.img_rect2[0] > 295:
            self.img_rect2.move_ip(-self.speed, 0)
            self.car_socket.left_socket()

    def move_right(self):
        '''
        right
        '''
        # Determine the x-direction position of the rectangle object
        if self.img_rect2[0] < 485:
            # change button direction
            self.img_rect2.move_ip(self.speed, 0)
            # send data
            self.car_socket.right_socket()

    def move_up(self):
        '''
        up
        '''
        # Determine the Y-direction position of the rectangle object
        if self.img_rect1[1] > 44:
            self.img_rect1.move_ip(0, -self.speed)
            self.car_socket.up_socket()

    def move_down(self):
        '''
        down
        '''
        # Determine the Y-direction position of the rectangle object
        if self.img_rect1[1] < 235:
            self.img_rect1.move_ip(0, self.speed)
            self.car_socket.down_socket()


class Windows(object):
    '''
    create window fram
    '''
    # 初始化
    def __init__(self):
        # initialization
        pygame.init()
        self.window = pygame.display.set_mode([640, 320])
        # initialize background
        pygame.display.set_caption('Control Panel')
        self.image = pygame.image.load('car.png')
        self.point_img = Point()

    def draw(self):
        '''
        Put the background and buttons in the main window
        '''
        self.window.blit(self.image, (0, 0))
        self.window.blit(self.point_img.image_point1, (self.point_img.img_rect1[0], self.point_img.img_rect1[1]))
        self.window.blit(self.point_img.image_point2, (self.point_img.img_rect2[0], self.point_img.img_rect2[1]))

    def event(self):
        '''
        Detect and respond to events
        '''
        # Get the current event type
        self.event_list = pygame.event.get()
        for event in self.event_list:
            if event.type == pygame.QUIT:
                self.game_over()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.point_img.move_up()
                    print('speed up--')
                if event.key == pygame.K_DOWN:
                    self.point_img.move_down()
                    print('speed down--')
                if event.key == pygame.K_LEFT:
                    self.point_img.move_left()
                    print('left--')
                if event.key == pygame.K_RIGHT:
                    self.point_img.move_right()
                    print('right--')

    def update(self):
        '''
        update
        '''
        pygame.display.update()

    def game_over(self):
        '''
        system exist
        '''
        pygame.quit()
        sys.exit()

    def run(self):
        '''
        programming running entry
        '''
        while True:
            self.draw()
            self.event()
            self.update()


if __name__ == '__main__':
    mower = Windows()
    mower.run()
