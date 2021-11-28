from typing import List
from rubyrobots.field import Field
from rubyrobots.robotPosition import RobotPosition
from rubyrobots.direction import Direction
from rubyrobots.robotCommand import RobotCommand


class RobotMovement:

    def __init__(self, field: Field, initialPosition: RobotPosition):
        if not field.validPosition(initialPosition):
            raise ValueError('Robot starting point is not in the field region')
        self.field: Field = field
        self.initialPosition: RobotPosition = initialPosition

    def moveRobot(self, commands: List[RobotCommand]):

        for command in commands:
            if command == RobotCommand.MOVE:
                self.move()
            if command == RobotCommand.RIGHT:
                self.rightTurn()
            if command == RobotCommand.LEFT:
                self.leftTurn()

    def leftTurn(self):
        if self.initialPosition.direction == Direction.NORTH:
            self.initialPosition.direction = Direction.WEST
        elif self.initialPosition.direction == Direction.SOUTH:
            self.initialPosition.direction = Direction.EAST
        elif self.initialPosition.direction == Direction.WEST:
            self.initialPosition.direction = Direction.SOUTH
        elif self.initialPosition.direction == Direction.EAST:
            self.initialPosition.direction = Direction.NORTH
        return self.initialPosition

    def rightTurn(self):
        if self.initialPosition.direction == Direction.NORTH:
            self.initialPosition.direction = Direction.EAST
        elif self.initialPosition.direction == Direction.SOUTH:
            self.initialPosition.direction = Direction.WEST
        elif self.initialPosition.direction == Direction.WEST:
            self.initialPosition.direction = Direction.NORTH
        elif self.initialPosition.direction == Direction.EAST:
            self.initialPosition.direction = Direction.SOUTH
        return self.initialPosition

    def move(self):
        if self.initialPosition.direction == Direction.NORTH:
            self.initialPosition.Y = self.initialPosition.Y + 1
        elif self.initialPosition.direction == Direction.SOUTH:
            self.initialPosition.Y = self.initialPosition.Y - 1
        elif self.initialPosition.direction == Direction.WEST:
            self.initialPosition.X = self.initialPosition.X - 1
        elif self.initialPosition.direction == Direction.EAST:
            self.initialPosition.X = self.initialPosition.X + 1

        if not self.field.validPosition(self.initialPosition):
            raise ValueError('Robot is moving out of the field region')
        return self.initialPosition
