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

def successorFunc(location, fringe):
    print("fill me in")


def positionInitialization(bfsmap):
    start = [0,0]
    goal = [0,0]

    for row in range(len(bfsmap)):
        for col in range(len(bfsmap[row])):
            if bfsmap[row][col] == 'R':
                start = (row,col)
            if bfsmap[row][col] == 'D':
                goal = (row,col)
    return start, goal


def bfsMazeSolution(bfsmap):
    start, goal = positionInitialization(bfsmap)
    print("start, goal: {}, {}".format(start, goal))
    pathCount = 1
    fringe = [[start]]
    print("fringe: {}".format(fringe))
    goalfound = False
    paths = [[]]




map1 = [[1, 1, 1, 1, 1, 1], [1, 0, 0, 0, "R", 1], [1, 0, 0, 0, 0, 1], [1, "D", 0, 0, 0, 1], [1, 1, 1, 1, 1]]
bfsMazeSolution(map1)
