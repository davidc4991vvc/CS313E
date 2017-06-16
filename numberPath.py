#  File:                numberPath.py
#  Description:         Finds a path through the maze whose sum equals the target.
#                       
#  Student's Name:      Nicolas Key
#  Student's UT EID:    
#  Course Name:         CS 313E 
#  Unique Number:       51915
#
#  Date Created:        4/10/2017
#  Date Last Modified:  4/14/2017



class State():

#    def __init__(self, start, end, target, grid_rows, grid_cols, grid):
#        self.start = start
#        self.end = end
#        self.target = target
#        self.grid_rows = grid_rows
#        self.grid_cols = grid_cols
#        self.grid = grid
#        self.history = [start]

    def __str__(self):
        myStr = "Start: " + str(self.start) + "\n"
        myStr = myStr + "End:   " + str(self.end) + "\n"
        myStr = myStr + "Target Value: " + str(self.target) + "\n"
        myStr = myStr + "Current sum: " + str(self.sum) + "\n"
        myStr = myStr + "History: " + str(self.numHistory) + "\n"
        myStr = myStr + "Grid Size: " + str(self.grid_rows) + " x " + str(self.grid_cols) + "\n"

        for row in range(self.grid_rows):
            for col in range(self.grid_cols):
                myStr = myStr + str(self.grid[row][col]) + " "
            myStr = myStr + "\n"

        return myStr

class Coordinate():

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __str__(self):
        return("(" + str(self.row) + ", " + str(self.col) + ")")

    def __eq__(self, other):
        if(self.row == other.row and self.col == other.col):
            return True
        return False

def isValidMove(cState, newCoord):
    #print(str(newCoord))
    if((newCoord.row < 0) or (newCoord.row > cState.grid_rows - 1) or (newCoord.col < 0) or (newCoord.col > cState.grid_cols - 1)):
        return False
    if(cState.grid[newCoord.row][newCoord.col] == None):
        return False
    return True


def solve(cState):

    #check if current location is goal and is target
    if(cState.start == cState.end):
        if(cState.target == cState.sum):
            print("Found!")
            myHist = ""
            count = 0
            for coord in cState.history:
                #print(str(coord))
                #print(myHist)
                myHist = myHist + str(coord) + " "
                count += 1
                if count % 10 == 0:
                    myHist = myHist + "\n"
            #print(myHist)
            print(str(cState.numHistory))
            return(myHist)
        #return None

    #move right
    if(isValidMove(cState, Coordinate(cState.start.row, cState.start.col + 1))):
        newState = State()
        newState.grid_rows = cState.grid_rows
        newState.grid_cols = cState.grid_cols
        newState.start = Coordinate(cState.start.row, cState.start.col + 1)
        newState.end = Coordinate(cState.end.row, cState.end.col)
#        newState.target = cState.target - cState.grid[cState.start.row][cState.start.col]
        newState.target = cState.target
        newState.sum = cState.sum + cState.grid[cState.start.row][cState.start.col + 1]
        newState.history = cState.history[:]
        newState.history.append(newState.start)
        newState.numHistory = cState.numHistory[:]
        newState.numHistory.append(cState.grid[cState.start.row][cState.start.col + 1])

        newState.grid = [r[:] for r in cState.grid]
        newState.grid[cState.start.row][cState.start.col] = None
        print(newState)
        if(newState.target >= newState.sum):
            path = solve(newState)
            if(path != None):
                return path
        else:
            print("None")
        

    #move up
    if(isValidMove(cState, Coordinate(cState.start.row - 1, cState.start.col))):
        newState = State()
        newState.grid_rows = cState.grid_rows
        newState.grid_cols = cState.grid_cols
        newState.start = Coordinate(cState.start.row - 1, cState.start.col)
        newState.end = Coordinate(cState.end.row, cState.end.col)
#        newState.target = cState.target - cState.grid[newState.start.row][newState.start.col]
        newState.target = cState.target
        newState.sum = cState.sum + cState.grid[cState.start.row - 1][cState.start.col]
        newState.history = cState.history[:]
        newState.history.append(newState.start)
        newState.numHistory = cState.numHistory[:]
        newState.numHistory.append(cState.grid[cState.start.row - 1][cState.start.col])

        newState.grid = [r[:] for r in cState.grid]
        newState.grid[cState.start.row][cState.start.col] = None
        print(newState)
        if(newState.target >= newState.sum):
            path = solve(newState)
            if(path != None):
                return path

    #move left
    if(isValidMove(cState, Coordinate(cState.start.row, cState.start.col - 1))):
        newState = State()
        newState.grid_rows = cState.grid_rows
        newState.grid_cols = cState.grid_cols
        newState.start = Coordinate(cState.start.row, cState.start.col - 1)
        newState.end = Coordinate(cState.end.row, cState.end.col)
#        newState.target = cState.target - cState.grid[newState.start.row][newState.start.col]
        newState.target = cState.target
        newState.sum = cState.sum + cState.grid[cState.start.row][cState.start.col - 1]
        newState.history = cState.history[:]
        newState.history.append(newState.start)
        newState.numHistory = cState.numHistory[:]
        newState.numHistory.append(cState.grid[cState.start.row][cState.start.col - 1])

        newState.grid = [r[:] for r in cState.grid]
        newState.grid[cState.start.row][cState.start.col] = None
        print(newState)
        if(newState.target >= newState.sum):
            path = solve(newState)
            if(path != None):
                return path

    #move down
    if(isValidMove(cState, Coordinate(cState.start.row + 1, cState.start.col))):
        newState = State()
        newState.grid_rows = cState.grid_rows
        newState.grid_cols = cState.grid_cols
        newState.start = Coordinate(cState.start.row + 1, cState.start.col)
        newState.end = Coordinate(cState.end.row, cState.end.col)
#        newState.target = cState.target - cState.grid[newState.start.row][newState.start.col]
        newState.target = cState.target
        newState.sum = cState.sum + cState.grid[cState.start.row + 1][cState.start.col]
        newState.history = cState.history[:]
        newState.history.append(newState.start)
        newState.numHistory = cState.numHistory[:]
        newState.numHistory.append(cState.grid[cState.start.row + 1][cState.start.col])

        newState.grid = [r[:] for r in cState.grid]
        newState.grid[cState.start.row][cState.start.col] = None
        print(newState)
        if(newState.target >= newState.sum):
            path = solve(newState)
            if(path != None):
                return path

    #else return invalid path
    return None


def main():
    file = open("pathdata.txt")
    line = file.readline()
    splitLine = line.split()
    targetValue = int(splitLine[0])
    grid_rows = int(splitLine[1])
    grid_cols = int(splitLine[2])
    start_row = int(splitLine[3])
    start_col = int(splitLine[4])
    end_row = int(splitLine[5])
    end_col = int(splitLine[6])

    maze = []
    index = 0
    while(index <= grid_rows):
        splitLine = file.readline().split()
        myList = []
        for num in range(len(splitLine)):
            myList.append(int(splitLine[num]))
        maze.append(myList)
        index += 1

    start = Coordinate(start_row, start_col)
    end = Coordinate(end_row, end_col)

    #myState = State(start, end, targetValue, grid_rows, grid_cols, maze)
    myState = State()
    myState.start = start
    myState.end = end
    myState.target = targetValue
    myState.grid_rows = grid_rows
    myState.grid_cols = grid_cols
    myState.grid = maze
    myState.history = [start]
    myState.numHistory = []
    myState.numHistory.append(myState.grid[myState.start.row][myState.start.col])
    myState.sum = myState.grid[myState.start.row][myState.start.col]

    print(myState)
 #   myState.target -= myState.grid[myState.start.row][myState.start.col]
    

#    print(str(myState))
    path = solve(myState)
    if(path == None):
        print("No valid path found.")
    else:
        print(path)


    
main()
