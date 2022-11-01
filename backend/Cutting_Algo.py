import array as arr
from Driver import Driver


class Cutting_Algo:
    def __init__(self, width, length, array):
        self.width = width
        self.length = length
        self.endpoint = False
        self.grassDesign = array
        self.val = 0
        self.cut = False
        drive = Driver()

    def driveInstructions(self):
        for row in self.length:
            if (self.endpoint == False):
                for column in reversed(self.width):
                    val = self.grassDesign[row][column]
                    if (val == 0):
                        self.cut = False
                    else:
                        self.cut = True
                    self.drive.rotateWheels()
                    self.drive.brake()
                self.endpoint = True
            else:
                for column in self.width:
                    # move
                    val = self.grassDesign[row][column]
                    if (val == 0):
                        self.cut = False
                    else:
                        self.cut = True
                    self.drive.rotateWheels()
                    self.drive.brake()
                self.endpoint = False
            if (self.endpoint == True):
                self.cut = False
                self.drive.turnRight()
                self.drive.rotateWheels()
                self.drive.brake()
                self.drive.turnRight()
            else:
                self.cut = True
                self.drive.turnLeft()
                self.drive.rotateWheels()
                self.drive.brake()
                self.drive.turnLeft()

    def findLengthOfFence(self):
        return self.length

    def findWidthOfFence(self):
        return self.width
