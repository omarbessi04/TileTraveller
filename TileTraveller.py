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
Invalid_direction = True

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

while coordinates_of_player != [3, 1]:
    N, S, E, W = False
    Valid_directions = []
    
    #Checks_Valid_directions
    for i in range(len(directions)):
        if coordinates_of_player in (directions)[i]:

            if (directions)[i] == directions[0]:
                N = True
                Valid_directions.append("(N)orth")

            if (directions)[i] == directions[1]:
                S = True
                Valid_directions.append("(S)outh")

            if (directions)[i] == directions[2]:
                E = True
                Valid_directions.append("(E)ast")

            if (directions)[i] == directions[3]:
                W = True
                Valid_directions.append("(W)est")

    print("You can travel: ", " or ".join(Valid_directions))
    player_move = input("Direction: ")

    if player_move.lower() == "n":
        if N:
            goNorth()
            Invalid_direction = False
        else:
            Invalid_direction = True

    elif player_move.lower() == "s":
        if S:
            goSouth()
            Invalid_direction = False
        else:
            Invalid_direction = True

    elif player_move.lower() == "e":
        if E:
            goEast()
            Invalid_direction = False
        else:
            Invalid_direction = True

    elif player_move.lower() == "w":
        if W:
            goWest()
            Invalid_direction = False
        else:
            Invalid_direction = True

    if Invalid_direction:
        print("Not a valid direction!")
    else:
        Valid_directions = []

print("Victory!")