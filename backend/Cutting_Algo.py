import array as arr


class Cutting_Algo:
    def __init__(self, width, length, array):
        self.width = width
        self.length = length
        self.endpoint = False
        self.grassDesign = array
        self.val = 0
        self.cut = False

    def driveInstructions(self):
        for row in self.length:
            if (self.endpoint == False):
                for column in reversed(self.width):
                    val = self.grassDesign[row][column]
                    if (val == 0):
                        self.cut = False
                    else:
                        self.cut = True
                # call mower
                # rotateWheels()
                # brake()
            else:
                for column in self.width:
                    # move
                    val = self.grassDesign[row][column]
                    if (val == 0):
                        self.cut = False
                    else:
                        self.cut = True
                # call mower
                # rotateWheels
                # brake()
            if (self.endpoint == True):
                self.cut = False
                # turnRight()
                # rotateWheels()
                # brake()
                # turnRight()
            else:
                self.cut = True
                # turnLeft()
                # rotateWheels()
                # brake()
                # turnLeft()

    def findLengthOfFence(self):
        return self.length

    def findWidthOfFence(self):
        return self.width
