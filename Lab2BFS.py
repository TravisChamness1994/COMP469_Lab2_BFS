# class BfsSolution:
#     map = [[]]
#     def __init__(self, mapFile):


#
# map[[]] = ""
# def readFile(fileHandle):
#     f = open(fileHandle)
#     index = 0
#     for x in f:
#         map[index] = x
#         index+= 1
#
# readFile("Map2.txt")


# Cartesian coordinate X and Y (X, Y) accessed from array
X = 0
Y = 1
COORD_MANIPULATOR_INIT = 1

#Incomplete Function
#Determines successor movements for the agent
def successorFunc(location, fringe, bfsMap):
    coordManipulator = COORD_MANIPULATOR_INIT
    branchList = []
    #check up - Negative Y direction: should never be out of bounds of the map, as long as the map is configured correctly
    if bfsMap[location[X]][(location[Y] - 1)] != 1:
        print("found free space going up!")
        while bfsMap[location[X], location[Y] - COORD_MANIPULATOR_INIT] != 1:
            coordManipulator = coordManipulator - 1
        branchList.append((location[X], location[coordManipulator + 1]))
    #check down
    coordManipulator = COORD_MANIPULATOR_INIT
    if bfsMap[location[X]][location[Y] + coordManipulator]:
        print("found free space going down!")
        while bfsMap[location[X]][location[Y] + coordManipulator] != 1:
            coordManipulator += 1
        print("Move down to ({}, {})".format(location[X], location[coordManipulator - 1]))
        branchList.append((location[X],location[coordManipulator - 1]))
        print(branchList)

#Note about row and col: row is the Y coordinate, and col is our X. It looks funny flipping order
#   going from accessor use in bfsMap[row][col] to cartesian assignment with (col, row), but it is correct
#   Feel free to double check, Juan.
def positionInitialization(bfsmap):
    start = [0,0]
    goal = [0,0]

    for row in range(len(bfsmap)):
        for col in range(len(bfsmap[row])):
            if bfsmap[row][col] == 'R':
                start = (col,row)
            if bfsmap[row][col] == 'D':
                goal = (col,row)
    return start, goal


def buildSolutions(start, goal, fringe, pathCount, paths):
    goalFound = False
    # while(not goalFound and fringe):
        # for path in range(pathCount):


def bfsMazeSolution(bfsmap):
    start, goal = positionInitialization(bfsmap)
    # print("start, goal: {}, {}".format(start, goal))
    pathCount = 1
    fringe = [[start]]
    # print("fringe: {}".format(fringe))
    paths = [[]]
    successorFunc(start, fringe, bfsmap)




map1 = [[1, 1, 1, 1, 1, 1], [1, 0, 0, 0, "R", 1], [1, 0, 0, 0, 0, 1], [1, "D", 0, 0, 0, 1], [1, 1, 1, 1, 1]]
bfsMazeSolution(map1)
