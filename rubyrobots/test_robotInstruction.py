from rubyrobots.robotInstruction import RobotInstruction
from rubyrobots.robotPosition import RobotPosition
from rubyrobots.direction import Direction
from rubyrobots.robotCommand import RobotCommand
import unittest

class Test_RobotInstruction(unittest.TestCase):

    def test_returnInstructionString(self):
        # Given
        instruction = RobotInstruction(RobotPosition(2, 2, Direction.NORTH),
                                       [RobotCommand.MOVE, RobotCommand.LEFT])
        expectedString = '2 2 N' + '\n' + 'ML'
        result = instruction.toString()

        self.assertAlmostEqual(result, expectedString)

if __name__ == '__main__':
    unittest.main()
