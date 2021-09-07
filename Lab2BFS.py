COL = 1
ROW = 0
# COORD_MANIPULATOR_INIT = 1

#Determines successor movements for the agent
def successorFunc(location, fringe, bfsMap, paths, path):
    #Branchlist is the list of possible branches or moves that are produced in the successor function
    # based off of the current location
    branchList = []
    #check up
    #Checking direction code pieces operate by first getting a deep copy of the original location.
    # by subtracting or adding to the column or row, it manipulates the section of the map matrix being looked at.
    print("Location: ", location)
    copyLocation = location.copy()
    #If the immediate dierection is not a wall
    if bfsMap[copyLocation[ROW] - 1][(copyLocation[COL])] != 1:
        copyLocation[ROW] = copyLocation[ROW] - 1
        #continue to step in the direction until a wall is contacted
        while bfsMap[copyLocation[ROW] - 1][copyLocation[COL]] != 1:
            copyLocation[ROW] = copyLocation[ROW] - 1
        #Once we find a wall, if the location at that point is not already visisted, add it to the branch list
        # NOTE: Branch list is the possible successor moves
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
    #add new branch list to fringe. If it is empty, it will not effect the fringe, otherwise new possible moves are added
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


#Build Solution function
# Looping until either the goal is found or the fringe is empty,
# iterate over the fringe for the existing amount of paths.
# Over each path, a set of possible moves exist with a minimum of 1.
# each move will be treated as a new current location
# As a new current location, the successor function will be run on that location, and the fringe will be updated.
# Once done, we add the location to the associated path (this is where the error probably occurs. Need a test where a path closes)
# Then test the location against the goal.
def buildSolutions(start, goal, fringe, pathCount, paths, bfsMap):
    goalFound = False
    successfulPath = []
    iter = 1
    while(not goalFound and fringe):
        print("ITERATION ", iter)
        pathCount = len(paths)
        print("FRINGE at first loop",fringe)
        print("Pathcount {} Paths {}".format(len(paths), paths))
        for path in range(pathCount):
            # Note on Condtional in this style: Not good, this should be replaced with a while loop. The forloop can be entered
            # regardless of goalFound being True because it is not a conditional of the looping structure. However, it will not run its course,
            # but none the less should not be entered at all.
            if not goalFound: #Conditional added to simulate a complex for loop conditional
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
            else: break #Acts as the end to the forloop if conditional is met

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
# map3 = [[1,1,1,1,1,1,1], [1,1,1,0,0,"R",1], [1,0,0,0,0,0,1], [1,0,0,0,0,0,1], [1,0,0,0,0,0,1], [1,1,1,0,1,1,1], [1,0,0,0,0,0,1], [1,0,1,1,1,"D",1], [1,1,1,1,1,1,1]]
professorsMap = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0, 0, 'R', 1], [1, 0, 0, 0, 0, 0, 0, 0, 1] , [1, 0, 0, 0, 0, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 'D', 1] , [1, 1, 1, 1, 1, 1, 1, 1, 1]]
# bfsMazeSolution(map1)
# bfsMazeSolution(map2)
# bfsMazeSolution(map3)
bfsMazeSolution(professorsMap)
