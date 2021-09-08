#Creators: Juan Zarate Hernandez & Travis Chamness
#Date: Sept 8, 2021
#Lab2: Maze Solution using BFS

COL = 1
ROW = 0

#Determines successor movements for the agent
def successorFunc(location, fringe, bfsMap, paths, path, nonContributor):
    #Branchlist is the list of possible branches or moves that are produced in the successor function
    # based off of the current location
    branchList = []
    #check up
    #Checking direction code pieces operate by first getting a deep copy of the original location.
    # by subtracting or adding to the column or row, it manipulates the section of the map matrix being looked at.
    copyLocation = location.copy()
    #If the immediate dierection is not a wall
    if bfsMap[copyLocation[ROW] - 1][(copyLocation[COL])] != 1:
        copyLocation[ROW] = copyLocation[ROW] - 1
        #continue to step in the direction until a wall is contacted
        while bfsMap[copyLocation[ROW] - 1][copyLocation[COL]] != 1:
            copyLocation[ROW] = copyLocation[ROW] - 1
        #Once we find a wall, if the location at that point is not already visisted, add it to the branch list
        # NOTE: Branch list is the possible successor moves
        if copyLocation not in paths[path]:
            branchList.append([copyLocation[ROW], copyLocation[COL]])
    #check down
    copyLocation = location.copy()
    if bfsMap[copyLocation[ROW] + 1][copyLocation[COL]] != 1:
        copyLocation[ROW] += 1
        while bfsMap[copyLocation[ROW] + 1][copyLocation[COL]] != 1:
            copyLocation[ROW] = copyLocation[ROW] + 1
        if copyLocation not in paths[path]:
            branchList.append([copyLocation[ROW], copyLocation[COL]])
    #check right
    copyLocation = location.copy()
    if bfsMap[copyLocation[ROW]][copyLocation[COL] + 1] != 1:
        copyLocation[COL] += 1
        while bfsMap[copyLocation[ROW]][copyLocation[COL] + 1] != 1:
            copyLocation[COL] += 1
        if copyLocation not in paths[path]:
            branchList.append([copyLocation[ROW], copyLocation[COL]])
    #check left
    copyLocation = location.copy()
    if bfsMap[copyLocation[ROW]][copyLocation[COL] - 1] != 1:
        copyLocation[COL] = copyLocation[COL] - 1
        while bfsMap[copyLocation[ROW]][copyLocation[COL] - 1] != 1:
            copyLocation[COL] = copyLocation[COL] - 1
        if copyLocation not in paths[path]:
            branchList.append([copyLocation[ROW], copyLocation[COL]])
    #add new branch list to fringe. If it is empty, it will not effect the fringe, otherwise new possible moves are added
    if branchList:
        fringe.append(branchList)
    else:
        nonContributor.append(path)
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
def buildSolutions(goal, fringe, pathCount, paths, bfsMap):
    goalFound = False
    successfulPath = []
    auxFringe = []
    nonContributor = []
    iter = 1
    while(not goalFound and fringe):
        pathCount = len(paths)
        for path in range(pathCount):
            #Conditional if-else added to simulate a complex for loop conditional
            # Note on Condtional in this style: Not good, this should be replaced with a while loop. The forloop can be entered
            # regardless of goalFound being True because it is not a conditional of the looping structure. However, it will not run its course,
            # but none the less should not be entered at all.
            if not goalFound:
                moves = fringe.pop(0)
                for index, move in enumerate(moves):
                    if index == 0:
                        fringe = successorFunc(move, fringe, bfsMap, paths, path, nonContributor)
                        paths[path].append(move)
                    else:
                        auxFringe = successorFunc(move, auxFringe, bfsMap, paths, path, nonContributor)
                        newPath = paths[path].copy()
                        newPath[len(newPath) - 1] = move
                        paths.append(newPath)

                    goalFound = goalTest(move, goal)
                    if goalFound:
                        successfulPath = paths[path + index]
                        break
            # 'else: break' acts as the end to the forloop if conditional is met. Understood to be not a good practice.
            else: break
        for badPath in nonContributor:
            paths.pop(badPath)
        for branches in auxFringe:
            fringe.append(branches)

        nonContributor = []
        auxFringe = []
        iter += 1
    return successfulPath, goalFound

def goalTest(location, goal):
    goalFound = False
    if location == goal:
        goalFound = True
    return goalFound

def bfsMazeSolution(bfsmap):
    start, goal = positionInitialization(bfsmap)
    print("start, goal: {}, {}".format(start, goal))
    fringe = [[start]]
    pathCount = 1
    paths = [[]]
    successfulPath, goalFound = buildSolutions(goal, fringe, pathCount, paths, bfsmap)
    cost = len(successfulPath)
    if goalFound:
        print("Successful Path is: {} with a cost of {}".format( successfulPath, cost))
    else:
        print("No path through maze found.")
    print("\n")
