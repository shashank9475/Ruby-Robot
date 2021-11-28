from mock import patch, mock_open
from rubyrobots.readInputFile import ReadInputFile
from rubyrobots.field import Field
from rubyrobots.robotInstruction import RobotInstruction
from rubyrobots.robotPosition import RobotPosition
from rubyrobots.direction import Direction
from rubyrobots.robotCommand import RobotCommand
from rubyrobots.error import Error
import unittest


class Test_ReadInputFile(unittest.TestCase):

    def test_raiseExceptionWhenFieldNotNumeric(self):
        filePath = 'abc.txt'
        mockedFileContent = '5 E\n3 3 E\nMMRMMRMRRM'

        readInputFile = ReadInputFile()

        with self.assertRaises(Error):
            with patch('builtins.open', mock_open(read_data=mockedFileContent)):
                readInputFile.readFile(filePath)

    def test_raiseExceptionWhenInvalidFieldDimension(self):
        filePath = 'abc.txt'
        mockedFileContent = '5 5 6\n3 3 E\nMMRMMRMRRM'

        readInputFile = ReadInputFile()

        with self.assertRaises(Error):
            with patch('builtins.open', mock_open(read_data=mockedFileContent)):
                readInputFile.readFile(filePath)

    def test_raiseExceptionWhenInvalidInitialPositionCoordinates(self):
        filePath = 'abc.txt'
        mockedFileContent = '5 5 6\n3 S E\nMMRMMRMRRM'

        readInputFile = ReadInputFile()

        with self.assertRaises(Error):
            with patch('builtins.open', mock_open(read_data=mockedFileContent)):
                readInputFile.readFile(filePath)

    def test_raiseExceptionWhenInvalidInitialPositionDimension(self):
        filePath = 'abc.txt'
        mockedFileContent = '5 5 6\n3 3 5 E\nMMRMMRMRRM'

        readInputFile = ReadInputFile()

        with self.assertRaises(Error):
            with patch('builtins.open', mock_open(read_data=mockedFileContent)):
                readInputFile.readFile(filePath)

    def test_raiseExceptionWhenInvalidInitialPositionDirection(self):
        filePath = 'abc.txt'
        mockedFileContent = '5 5 6\n3 3 Y\nMMRMMRMRRM'

        readInputFile = ReadInputFile()

        with self.assertRaises(Error):
            with patch('builtins.open', mock_open(read_data=mockedFileContent)):
                readInputFile.readFile(filePath)


    def test_returnValidInstructions(self):
        filePath = 'abc.txt'
        mockedFileContent = '5 5\n3 3 E\nMMR\n2 2 N\nRMLM'

        readInputFile = ReadInputFile()

        field = Field(5, 5)
        robotCommands1 = [RobotCommand('M'), RobotCommand('M'), RobotCommand('R')]
        robotCommands2 = [RobotCommand('R'), RobotCommand('M'), RobotCommand('L'), RobotCommand('M')]
        robotInstruction1 = RobotInstruction(RobotPosition(3, 3, Direction('E')), robotCommands1)
        robotInstruction2 = RobotInstruction(RobotPosition(2, 2, Direction('N')), robotCommands2)

        expected_field_size = '5 5'
        expectedRobotInstructions = [robotInstruction1, robotInstruction2]

        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            field_size, robot_instructions = readInputFile.readFile(filePath)

        self.assertAlmostEqual(field_size.toString(), expected_field_size)
        self.assertAlmostEqual(robot_instructions[0].toString(), expectedRobotInstructions[0].toString())
        self.assertAlmostEqual(robot_instructions[1].toString(), expectedRobotInstructions[1].toString())


    def test_raiseExceptionWhenInvalidMoveCommand(self):
        filePath = 'abc.txt'
        mockedFileContent = '5 5\n3 3 E\nMXRMMRMRRM'

        readInputFile = ReadInputFile()

        with self.assertRaises(ValueError):
            with patch('builtins.open', mock_open(read_data=mockedFileContent)):
                readInputFile.readFile(filePath)

if __name__ == '__main__':
    unittest.main()