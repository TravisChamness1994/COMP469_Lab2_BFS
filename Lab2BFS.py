COL = 1
ROW = 0
# COORD_MANIPULATOR_INIT = 1

#Incomplete Function
#Determines successor movements for the agent
def successorFunc(location, fringe, bfsMap, paths, path):
    branchList = []
    #check up
    print("Location: ", location)
    copyLocation = location.copy()
    if bfsMap[copyLocation[ROW] - 1][(copyLocation[COL])] != 1:
        copyLocation[ROW] = copyLocation[ROW] - 1
        while bfsMap[copyLocation[ROW] - 1][copyLocation[COL]] != 1:
            copyLocation[ROW] = copyLocation[ROW] - 1
        if [copyLocation[ROW], copyLocation[COL]] not in paths[path]:
            branchList.append([copyLocation[ROW], copyLocation[COL]])
    #check down
    copyLocation = location.copy()
    if bfsMap[copyLocation[ROW] + 1][copyLocation[COL]] != 1:
        copyLocation[ROW] += 1
        while bfsMap[copyLocation[ROW] + 1][copyLocation[COL]] != 1:
            copyLocation[ROW] = copyLocation[ROW] + 1
        if [copyLocation[ROW], copyLocation[COL]] not in paths[path]:
            branchList.append([copyLocation[ROW], copyLocation[COL]])
    #check right
    copyLocation = location.copy()
    if bfsMap[copyLocation[ROW]][copyLocation[COL] + 1] != 1:
        copyLocation[COL] += 1
        while bfsMap[copyLocation[ROW]][copyLocation[COL] + 1] != 1:
            copyLocation[COL] += 1
        if [copyLocation[ROW], copyLocation[COL]] not in paths[path]:
            branchList.append([copyLocation[ROW], copyLocation[COL]])
    #check left
    copyLocation = location.copy()
    if bfsMap[copyLocation[ROW]][copyLocation[COL] - 1] != 1:
        copyLocation[COL] = copyLocation[COL] - 1
        while bfsMap[copyLocation[ROW]][copyLocation[COL] - 1] != 1:
            copyLocation[COL] = copyLocation[COL] - 1
        if [copyLocation[ROW], copyLocation[COL]] not in paths[path]:
            branchList.append([copyLocation[ROW], copyLocation[COL]])
    #add new branch list to fringe
    if branchList:
        fringe.append(branchList)
    #return new fringe
    return fringe

#Initializes the start location and goal location values
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


def buildSolutions(start, goal, fringe, pathCount, paths, bfsMap):
    goalFound = False
    successfulPath = []
    # print("FRINGE: ", fringe)
    iter = 1
    while(not goalFound and fringe):
        print("ITERATION ", iter)
        pathCount = len(paths)
        print("FRINGE at first loop",fringe)
        print("Pathcount {} Paths {}".format(len(paths), paths))
        for path in range(pathCount):
            # print("Path iteration = ", path)
            moves = fringe.pop(0)
            print("Moves in path {}: {}".format(path, moves))
            for index, move in enumerate(moves):
                fringe = successorFunc(move, fringe, bfsMap, paths, path)
                print("Fringe after successor: ", fringe)
                if index == 0:
                    paths[path].append(move)
                else:
                    newPath = paths[path].copy()
                    newPath[len(newPath) - 1] = move
                    paths.append(newPath)
                goalFound = goalTest(move, goal)
                if goalFound:
                    successfulPath = paths[path + index]
                    break
                print("PATHS: ",paths)
                print("End of iteration {}, Goal found = {}".format(iter, goalFound))

        iter += 1
    print("OUTSIDE WHILE LOOP")
    return successfulPath, goalFound

def goalTest(location, goal):
    goalFound = False
    print("GOAL TEST LOCATION: ",location)
    if location[ROW] == goal[ROW] and location[COL] == goal[COL]:
        print("GOAL TEST: TRUE")
        goalFound = True
    return goalFound

def bfsMazeSolution(bfsmap):
    start, goal = positionInitialization(bfsmap)
    print("start, goal: {}, {}".format(start, goal))
    fringe = [[start]]
    pathCount = 1
    paths = [[]]
    successfulPath, goalFound = buildSolutions(start, goal, fringe, pathCount, paths, bfsmap)

    if goalFound:
        print("Successful Path is: ", successfulPath)
    else:
        print("No path through maze found.")
    print("\n")



# map1 = [[1, 1, 1, 1, 1, 1], [1, "D", 0, 0, "R", 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1]]
# map2 = [[1, 1, 1, 1, 1, 1], [1, 0, 0, 0, "R", 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, "D", 1], [1, 1, 1, 1, 1, 1]]
professorsMap = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0, 0, 'R', 1], [1, 0, 0, 0, 0, 0, 0, 0, 1] , [1, 0, 0, 0, 0, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 'D', 1] , [1, 1, 1, 1, 1, 1, 1, 1, 1]]
# bfsMazeSolution(map1)
# bfsMazeSolution(map2)
bfsMazeSolution(professorsMap)
