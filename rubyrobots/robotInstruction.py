from typing import List
from rubyrobots.robotPosition import RobotPosition
from rubyrobots.robotCommand import RobotCommand


class RobotInstruction:

    def __init__(self, initialPosition: RobotPosition, robotCommands: List[RobotCommand]):
        self.initialPosition = initialPosition
        self.robotCommands = robotCommands

    def toString(self):
        movementCommands = ''.join([command.value for command in self.robotCommands])
        return self.initialPosition.toString() + '\n' + movementCommands


