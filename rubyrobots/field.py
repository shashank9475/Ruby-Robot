from rubyrobots.robotPosition import RobotPosition


class Field:

    def __init__(self, X: int, Y: int):
        self.X: int = X
        self.Y: int = Y

    def validPosition(self, position: RobotPosition):
        return not (position.X > self.X or position.Y > self.Y or position.X < 0 or position.Y < 0)

    def toString(self):
        return str(self.X) + ' ' + str(self.Y)
