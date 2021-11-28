from rubyrobots.robotMovement import RobotMovement
from rubyrobots.robotPosition import RobotPosition
from rubyrobots.direction import Direction
from rubyrobots.field import Field
from rubyrobots.robotCommand import RobotCommand
import unittest


class Test_Rover(unittest.TestCase):

    def test_robotFinalPositionAfterMovement(self):

        initialPosition = RobotPosition(2, 2, Direction.NORTH)
        field = Field(5, 5)
        commands = [RobotCommand.RIGHT,
                            RobotCommand.RIGHT,
                            RobotCommand.MOVE,
                            RobotCommand.LEFT,
                            RobotCommand.LEFT]
        robotMovement = RobotMovement(field, initialPosition)

        robotMovement.moveRobot(commands)

        expectedFinalPosition = '2 1 N'

        self.assertAlmostEqual(initialPosition.toString(),expectedFinalPosition)


    def test_robotInitialPositionOutOfField(self):
        initialPosition = RobotPosition(15, 2, Direction.NORTH)
        field = Field(10, 10)

        with self.assertRaises(ValueError):
            robotMovement = RobotMovement(field, initialPosition)

    def test_robotFinalPositionOutOfField(self):
        initialPosition = RobotPosition(9, 2, Direction.EAST)
        field = Field(10, 10)
        commands = [RobotCommand.MOVE,
                    RobotCommand.MOVE,
                    RobotCommand.RIGHT]
        robotMovement = RobotMovement(field, initialPosition)

        with self.assertRaises(ValueError):
            robotMovement.moveRobot(commands)

if __name__ == '__main__':
    unittest.main()