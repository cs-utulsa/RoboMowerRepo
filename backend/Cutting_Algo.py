import array as arr
from clience import Point
from server import CarPi


class Cutting_Algo:

    def __init__(self, width, length, array):
        self.width = width
        self.length = length
        self.endpoint = False
        self.grassDesign = array
        self.val = 0
        self.cut = False
        self.moveDirection = CarPi()

    def clientDirectionInstructions(self):
        for row in self.length:
            if (self.endpoint == False):
                for column in reversed(self.width):
                    val = self.grassDesign[row][column]
                    if (val == 0):
                        self.cut = False
                    else:
                        self.cut = True
                    self.moveDirection.moveDirection('up')
                self.endpoint = True
            else:
                for column in self.width:
                    val = self.grassDesign[row][column]
                    if (val == 0):
                        self.cut = False
                    else:
                        self.cut = True
                    self.moveDirection.moveDirection('up')
                self.endpoint = False
            if (self.endpoint == True):
                self.cut = False
                self.moveDirection.moveDirection('right')
                self.moveDirection.moveDirection('up')
                self.moveDirection.moveDirection('right')
            else:
                self.cut = True
                self.moveDirection.moveDirection('left')
                self.moveDirection.moveDirection('up')
                self.moveDirection.moveDirection('left')

    def findLengthOfFence(self):
        return self.length

    def findWidthOfFence(self):
        return self.width

    # results(self):

    # def caculateTime(self):
