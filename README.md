RUBY ROBOTS

Prototypes of a squad of ruby robot should be developed. A ruby robot is a robot which is able to explore and interact with the outer world in some  degree by moving and exploring. We want to navigate our Ruby Robots through an open field and test its Geo cache mapping functionality.

Our robots position is represented by a combination of an x and y co-ordinates and a letter representing one of the four cardinal compass points. The test field is divided up into a grid to simplify navigation. An example position might be 1, 1, N, meaning our robot is in the bottom left corner and facing North.

In order to control the ruby robot,we can send a simple string of letters. The only valid possible letters are 'L', 'R' and 'M'. 'L' and 'R' makes our robot spin 90 degrees left or right respectively, without moving from its current position.

'M' means move forward one grid point, and maintain the same heading.

Assume that the square directly North from (x, y) is (x, y+1).

Input:

The first line of input is the upper-right coordinates of the test field, the lower-left coordinates are assumed to be 0,0.

The rest of the input is information to the robots that have been deployed. Each robot has two lines of input. The first line gives the robot's position, and the second line is a series of instructions telling the robot how to explore the test field.

The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the robot orientation.

Each robot run will be finished sequentially, which means that the second robot run can not start to move until the first one has finished.

Output:

The output for each robot should be its final co-ordinates and heading.


Test Input:

10 10

2 3 E

RMRMRLMRMRMRMR

5 4 W

LMRMLMRMRLMRRM


Expected Output:

1 2 W

3 2 E

#  Installing

Requirements : Python3, pip, mock, unittest


#  How to run
   Insert field size, robot initial position and robot command in test.txt file
   python3 run.py

This will print the final robot position
    
#  Run test cases

   python3 -m unittest <python file to test>
