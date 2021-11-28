from rubyrobots.robotPosition import RobotPosition
from rubyrobots.direction import Direction
import unittest

class Test_RobotPosition(unittest.TestCase):

    def test_returnPositionString(self):
        # Given
        position = RobotPosition(4, 6, Direction.NORTH)
        expectedString = '4 6 N'
        result = position.toString()
        self.assertAlmostEqual(result, expectedString)

if __name__ == '__main__':
    unittest.main()
