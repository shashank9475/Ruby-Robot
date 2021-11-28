from rubyrobots.robotMovement import RobotPosition
from rubyrobots.field import Field
from rubyrobots.robotInstruction import RobotInstruction
from rubyrobots.direction import Direction
from rubyrobots.error import Error
from rubyrobots.robotCommand import RobotCommand
import re


class ReadInputFile:

    validfieldsize = re.compile("^[0-9]* [0-9]*$")
    validRobotPosition = re.compile("^[0-9]* [0-9]* [NSEW]$")

    def readFile(self, filePath):
        with open(filePath, 'r') as file:
            field = file.readline()
            field_size = self.field_input(field)

            robotInstructions = []
            for lineCount, line in enumerate(file, start=1):
                if lineCount % 2 != 0:
                    robotInitialPosition = self.getInitialPosition(line)
                else:
                    movement_commands = self.getMoveCommands(line)
                    instructions = RobotInstruction(robotInitialPosition, movement_commands)
                    robotInstructions.append(instructions)
        return field_size, robotInstructions

    def field_input(self, inputField):
        if not re.match(self.validfieldsize, inputField):
            raise Error("Invalid field dimensions")
        inputFieldList = inputField.split(" ")
        return Field(int(inputFieldList[0]), int(inputFieldList[1]))

    def getInitialPosition(self, line):
        if not re.match(self.validRobotPosition, line):
            raise Error("Invalid robot initial position")
        initialPositionList = line.split()
        return RobotPosition(int(initialPositionList[0]),
                             int(initialPositionList[1]),
                             Direction(initialPositionList[2]))

    def getMoveCommands(self, line):
        commands = [RobotCommand(command) for command in list(line.replace('\n', ''))]
        return commands


