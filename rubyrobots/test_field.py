from rubyrobots.field import Field
import unittest

class Test_Field(unittest.TestCase):

    def test_returnFieldString(self):
        field = Field(3, 3)
        exptectedFieldAsString = '3 3'

        result = field.toString()
        self.assertAlmostEqual(exptectedFieldAsString, result)

if __name__ == '__main__':
    unittest.main()