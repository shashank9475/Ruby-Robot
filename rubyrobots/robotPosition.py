from rubyrobots.direction import Direction


class RobotPosition:

    def __init__(self, X, Y, dir: Direction):
        self.X = X
        self.Y = Y
        self.direction = dir

    def toString(self):
        return str(self.X) + " " + str(self.Y) + " " + self.direction.value
