"""
1. Describe the general outline of how you're going to develop this program, and
commit it.
2. Then gradually break it down into more detailed steps (committing after each
comprehensive step),
until you start to see a way to convert this description into code.
"""
# 3. Then start writing the code

x = 1
y = 1
coordinates_of_player = [x,y]
#functions that move player
def goNorth():
    y += 1

def goSouth():
    y -= 1

def goEast():
    x += 1

def goWest():
    x -= 1

#list of all the tiles that are available
directions = [[[1,1][1,2][2,1][3,1][3,2]], [[1,2][1,3][2,2][3,3][3,2]], [[1,3][1,2][2,3]], [[3,3][2,3][2,2]]]
