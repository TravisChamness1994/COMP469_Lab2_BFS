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
COL = 1
ROW = 0
# COORD_MANIPULATOR_INIT = 1

#Incomplete Function
#Determines successor movements for the agent
def successorFunc(location, fringe, bfsMap):
    branchList = []
    #check up
    copyLocation = location.copy()
    copyLocation[ROW] = copyLocation[ROW] - 1
    if bfsMap[copyLocation[ROW]][(copyLocation[COL])] != 1:
        while bfsMap[copyLocation[ROW]][copyLocation[COL]] != 1:
            copyLocation[ROW] = copyLocation[ROW] - 1
        branchList.append((location[ROW],  copyLocation[COL]))
    #check down
    copyLocation = location.copy()
    copyLocation[ROW] += 1
    if bfsMap[copyLocation[ROW]][copyLocation[COL]] != 1:
        print("found free space going down!")
        while bfsMap[copyLocation[ROW]][copyLocation[COL]] != 1:
            copyLocation[ROW] = copyLocation[ROW] + 1
        branchList.append((copyLocation[ROW] - 1, copyLocation[COL]))
        print(branchList)


def positionInitialization(bfsmap):
    start = [0,0]
    goal = [0,0]

    for row in range(len(bfsmap)):
        for col in range(len(bfsmap[row])):
            if bfsmap[row][col] == 'R':
                start = [row,col]
            if bfsmap[row][col] == 'D':
                goal = [row,col]
    return start, goal


def buildSolutions(start, goal, fringe, pathCount, paths):
    goalFound = False
    # while(not goalFound and fringe):
        # for path in range(pathCount):


def bfsMazeSolution(bfsmap):
    start, goal = positionInitialization(bfsmap)
    print("start, goal: {}, {}".format(start, goal))
    pathCount = 1
    fringe = [[start]]
    # print("fringe: {}".format(fringe))
    paths = [[]]
    successorFunc(start, fringe, bfsmap)




map1 = [[1, 1, 1, 1, 1, 1], [1, 0, 0, 0, "R", 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, "D", 0, 1], [1, 1, 1, 1, 1, 1]]
bfsMazeSolution(map1)
