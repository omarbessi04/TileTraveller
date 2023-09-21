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

#list of all the tiles that are available, N, S, E, W
directions = [[[1,1][1,2][2,1][3,1][3,2]], [[1,2][1,3][2,2][3,3][3,2]], [[1,3][1,2][2,3]], [[3,3][2,3][2,2]]]

available_direction = []
while coordinates_of_player != [3, 1]:
    available_direction = []
#Checks_available_directions
    for i in range(len(directions)):
        if coordinates_of_player in (directions)[i]:
            if (directions)[i] == directions[0]:
                available_direction.append("(N)orth")
            if (directions)[i] == directions[1]:
                available_direction.append("(S)outh")
            if (directions)[i] == directions[2]:
                available_direction.append("(E)ast")
            if (directions)[i] == directions[3]:
                available_direction.append("(W)est")


                

        

