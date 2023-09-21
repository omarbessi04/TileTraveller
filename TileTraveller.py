#functions that move player
def goNorth():
    global y, coordinates_of_player
    y += 1
    coordinates_of_player = [x,y]

def goSouth():
    global y, coordinates_of_player
    y -= 1
    coordinates_of_player = [x,y]

def goEast():
    global x, coordinates_of_player
    x += 1
    coordinates_of_player = [x,y]

def goWest():
    global x, coordinates_of_player
    x -= 1
    coordinates_of_player = [x,y]

def Check_Valid_Directions():
    for i in range(len(directions)):
        if coordinates_of_player in (directions)[i]:

            if (directions)[i] == directions[0]:
                Valid_directions.append("(N)orth")

            if (directions)[i] == directions[1]:
                Valid_directions.append("(S)outh")

            if (directions)[i] == directions[2]:
                Valid_directions.append("(E)ast")

            if (directions)[i] == directions[3]:
                Valid_directions.append("(W)est")

x = 1
y = 1
coordinates_of_player = [x,y]
Invalid_direction = True


#list of all the tiles that are available, N, S, E, W
directions = [[[1,1], [1,2], [2,1], [3,1], [3,2]],  [[1,2], [1,3], [2,2], [3,3], [3,2]],  [[1,3], [1,2], [2,3]],  [[3,3], [2,3], [2,2]]]
Valid_directions = []

Check_Valid_Directions()
print("You can travel: ", " or ".join(Valid_directions), end=".\n")

while coordinates_of_player != [3, 1]:

    Valid_directions = []
    Check_Valid_Directions()
    player_move = input("Direction: ")

    if player_move.lower() == "n":
        if "(N)orth" in Valid_directions:
            goNorth()
            Invalid_direction = False
        else:
            Invalid_direction = True

    elif player_move.lower() == "s":
        if "(S)outh" in Valid_directions:
            goSouth()
            Invalid_direction = False
        else:
            Invalid_direction = True

    elif player_move.lower() == "e":
        if "(E)ast" in Valid_directions:
            goEast()
            Invalid_direction = False
        else:
            Invalid_direction = True

    elif player_move.lower() == "w":
        if "(W)est" in Valid_directions:
            goWest()
            Invalid_direction = False
        else:
            Invalid_direction = True

    if Invalid_direction:
        print("Not a valid direction!")
    else:
        if coordinates_of_player != [3,1]:
            Valid_directions = []
            Check_Valid_Directions()
            print("You can travel: ", " or ".join(Valid_directions), end=".\n")

print("Victory!")