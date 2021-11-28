from rubyrobots.readInputFile import ReadInputFile
from rubyrobots.error import Error
from rubyrobots.robotMovement import RobotMovement


def main():
    test_file = 'test_file.txt'
    readInputFile = ReadInputFile()
    try:
        field_size, instructions = readInputFile.readFile(test_file)
        for instruction in instructions:
            robot = RobotMovement(field_size, instruction.initialPosition)
            robot.moveRobot(instruction.robotCommands)
            print(robot.initialPosition.toString())
    except Error as error:
        print(error)
    except ValueError as error:
        print(error)


if __name__ == '__main__':
    main()
