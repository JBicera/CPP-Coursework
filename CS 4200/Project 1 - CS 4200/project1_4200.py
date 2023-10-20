import random
import heapq
import copy
import time

#Class represents puzzle state as a node object with parent and children nodes
class StateNode:
    #Initialize StateNode Object
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
    
    #Defines how to equate nodes
    def __eq__(self, other):
        return self.state == other.state 
    
    #Defines how to convert node into key for storage in set
    def __hash__(self):
        return hash(self.state)
    
    #Defines how to compare objects
    def __lt__(self, other):
        return self.state.gCost + self.state.hCost < other.state.gCost + other.state.hCost
    def __le__(self,other):
        return self.state.gCost + self.state.hCost <= other.state.gCost + other.state.hCost
    
    #Adds child node function
    def addChild(self, child):
        self.children.append(child)

#Class represents current state of puzzle
class PuzzleState:
    #Initializes PuzzleState object 
    def __init__(self, board):
        self.board = board
        self.gCost = 0
        self.hCost = 0

    #Defines how to equate boards 
    def __eq__(self, other):
        return self.board == other.board 

    #Defines way to convert board configuration into a key for storing into a set
    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.board))

    #Defines how puzzle state object is represented as a string
    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.board])

    #Defines how to compare boards f(n) = g(n) + h(n)
    def __lt__(self, other):
        return self.gCost + self.hCost < other.gCost + other.hCost

    def copy(self):
        return copy.deepcopy(self)
    
    #Gets the position of the empty space in the board 
    def getEmptySpace(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j

    #When moving creates new board with blank space swapped with specified tile
    def move(self, rowMove, colMove):
        emptySpaceRow, emptySpaceCol = self.getEmptySpace()
        self.board[emptySpaceRow][emptySpaceCol], self.board[rowMove][colMove] = self.board[rowMove][colMove], self.board[emptySpaceRow][emptySpaceCol]
    
#Heuristic Functions h(n) = Estimated cost from n to goal
#Number of misplaced tiles compared to the goal state 
def h1(state, goalState):
    misplacedCount = 0
    for i in range (3):
        for j in range (3):
            #If current state board is different then there is a misplaced tile
            if state.board[i][j] != goalState.board[i][j]:
                misplacedCount += 1
    return misplacedCount

#Sum of distance of tiles from their goal positions aka Manhattan distance of each tile
def h2(state, goalState):
    totalDistance = 0
    #Iterate through board
    for i in range(3):
        for j in range(3):
            tile = state.board[i][j]
            if tile != 0:  #Ignore blank space
                for goalI in range(3):
                    for goalJ in range(3):
                        #Correct position is found
                        if goalState.board[goalI][goalJ] == tile:
                            #Get absolute distance of tile from its correct position
                            totalDistance += abs(goalI - i) + abs(goalJ - j)
                            break
    return totalDistance

#Generates random puzzle board
def generateRandPuzzle():
    numbers = list(range(9)) #Numbers 0-8 possible
    random.shuffle(numbers) #Shuffle list to make random
    board = []
    for i in range(0, 9, 3):
        board.append(numbers[i:i+3]) #Makes 3x3 board
    puzzle = PuzzleState(board) 
    #Ensure board is solvable 
    while not isSolvable(puzzle):
        random.shuffle(numbers) #Shuffle again
        board = []
        for i in range(0, 9, 3):
            board.append(numbers[i:i+3])
        puzzle = PuzzleState(board)
    return puzzle

#Check if the puzzle is solvable based on the inversion count
#Even inversion count == solvable
#Odd inversion count == unsolvable
def isSolvable(puzzle):
    #Iterates over every row in board then every num in every row and puts in new list
    boardList = [num for row in puzzle.board for num in row]
    inversionCount = 0
    for i in range(0,9):
        for j in range(i + 1, 9):
            #Check if any number is out of order and positions are non-zero
            if boardList[i] and boardList[j] and boardList[i] > boardList[j]:
                inversionCount += 1
    return inversionCount % 2 == 0

#Gets path of solution by going from bottom node all the way to the root
def traceNodes(goal):
    path = []
    current = goal
    while current is not None:
        path.append(current.state)
        current = current.parent
    path.reverse()
    return path
    
#A Star Search that utilizes heap queue
def aStarSearch(initState, goalState, heuristicFunction):
    initState.hCost = heuristicFunction(initState,goalState)
    rootNode = StateNode(initState)
    #Heap queue of State Node Objects
    frontier = [rootNode]
    #Set of explored State Node objects
    exploredSet = set()
    generatedNodes = 0
    #Iterate every child node that has the smallest f(n) value
    while frontier:
        currentNode = heapq.heappop(frontier)
        if currentNode.state == goalState:
            path = traceNodes(currentNode)
            return generatedNodes, path 

        exploredSet.add(hash(currentNode))

        #All possible moves that can be made from the empty space
        emptySpaceRow, emptySpaceCol = currentNode.state.getEmptySpace()
        possibleMoves = [
            (emptySpaceRow-1, emptySpaceCol), #Left
            (emptySpaceRow+1, emptySpaceCol), #Right
            (emptySpaceRow, emptySpaceCol+1), #Up
            (emptySpaceRow, emptySpaceCol-1)  #Down
        ]
        #Iterate through all possible moves
        for rowMove, colMove in possibleMoves: 
            if 0 <= rowMove < 3 and 0 <= colMove < 3: #Checks if move is possible
                newState = currentNode.state.copy() #Copy current board
                newState.move(rowMove, colMove) #Make move
                newState.gCost = currentNode.state.gCost + 1
                newState.hCost = heuristicFunction(newState, goalState)
                childNode = StateNode(newState, currentNode)

                #If newState is not already explored and is not yet in the frontier
                if hash(childNode) not in exploredSet and childNode not in frontier:
                    currentNode.addChild(childNode)
                    #Push the newState onto the frontier
                    heapq.heappush(frontier, childNode)
                    generatedNodes += 1
    return -1, None

#Prints solution path of every node from root to goal 
def printState(state, step):
    print("Step", step)
    for row in state.board:
        print("[", " ".join(map(str, row)), "]")
    print()

#Utility function to get valid integer inputs from a specified range
def getValidIntInput(prompt, min, max):
    while True:
        value = input(prompt)
        if value.isdigit() and min <= int(value) <= max:
            return int(value)
        print("Please enter valid integer(s): ")

#Get user input in one single line and convert it into a puzzle board
def getUserPuzzle():
    print("Enter your custom puzzle board as one line (e.g. '0 1 2 3 4 5 6 7 8'): ")
    #Separate by space
    userInput = input().strip().split()
    #Input Validation for puzzle board string
    while len(userInput) != 9 or not all(num.isdigit() for num in userInput):
        print("Please enter 9 integers.")
        userInput = getValidIntInput("",0,8).strip().split()
    board = [userInput[i:i+3] for i in range(0, 9, 3)]
    puzzle = PuzzleState([[int(num) for num in row] for row in board])
    return puzzle

#Function for option 1 testing one puzzle
def singleTestPuzzle():
    #Prompt for choice
    print("Select Input Method:")
    print("[1] Random")
    print("[2] User Input")
    userInput = getValidIntInput("", 1, 3)
    initState = None
    goalState = PuzzleState([[0, 1, 2], 
                             [3, 4, 5], 
                             [6, 7, 8]])
    #Get puzzle the algorithm is going to use
    if userInput == 1:
        initState = generateRandPuzzle()
    elif userInput == 2:
        initState = getUserPuzzle()
    #Decide what information to print out
    print("Select H Function:")
    print("[1] H1")
    print("[2] H2")
    print("[3] Both")
    hChoice = int(input())
    print("Initial Puzzle: ")
    printState(initState, 0)
    totalCost = 0
    totalCost2 = 0
    startTime = time.time()
    #Print only Heuristic 1
    if hChoice == 1:
        searchCost, path = aStarSearch(initState,goalState, h1)
        endTime = time.time()
        print("Solution Found")
        for step, state in enumerate(path, start=1):
            printState(state, step)
        runTime = endTime - startTime
        print("H1 Search Cost: ", searchCost)
        print("H1 Runtime: ",round(runTime* 1000,2), "milliseconds")
        print("\n")
        return
    #Print only Heuristic 2
    elif hChoice == 2:
        searchCost, path = aStarSearch(initState,goalState, h2)
        totalCost += searchCost
        endTime = time.time()
        print("Solution Found")
        for step, state in enumerate(path, start=1):
            printState(state, step)
        runTime = endTime - startTime
        print("H2 Search Cost: ", searchCost)
        print("H2 Runtime: ",round(runTime* 1000,2), "milliseconds")
        print("\n")
        return
    #Print both Heuristic Function results
    elif hChoice == 3:
        searchCost1, path = aStarSearch(initState,goalState, h1)
        endTime  = time.time()
        runTime1 = endTime - startTime
        print("Solution Found")
        for step, state in enumerate(path, start=1):
            printState(state, step)
        startTime = time.time()
        searchCost2, path = aStarSearch(initState,goalState, h2)
        endTime = time.time()
        print("Solution Found")
        for step, state in enumerate(path, start=1):
            printState(state, step)
        runTime2 = endTime - startTime
        print("H1 Search Cost: ", searchCost1)
        print("H1 Runtime: ",round(runTime1* 1000,2), "milliseconds")
        print("H2 Search Cost: ", searchCost2)
        print("H2 Runtime: ",round(runTime2* 1000,2), "milliseconds")
        print("\n")
        return
    
#Dissects file input into a list of puzzle states
def getFileInputStates(inputStr):
    #Ignore /// line
    inputLines = inputStr.strip().split("/////////////////////////////////////////////////////")
    puzzleStates = []
    #Store boards into list
    for puzzle_input in inputLines[1:]:
        rows = puzzle_input.strip().split("\n")
        board = [list(map(int, row.strip().split())) for row in rows]
        puzzle = PuzzleState(board)
        puzzleStates.append(puzzle)
    return puzzleStates     

#Gets file name from user then processes all in file for both heuristic functions
def calcFilePuzzles():
    totalCostH1 = 0
    totalCostH2 = 0
    goalState = PuzzleState([[0, 1, 2], 
                             [3, 4, 5], 
                             [6, 7, 8]])
    fileName = input("Please enter filename: ")
    with open(fileName, 'r') as file:
        inputStr = file.read()
    boardStates = getFileInputStates(inputStr)

    #Process Heuristic 1
    startTime1 = time.time()
    for puzzle in boardStates:
        searchCost1, path = aStarSearch(puzzle,goalState, h1)
        totalCostH1 += searchCost1
    endTime1  = time.time()
    runTime1 = endTime1 - startTime1 
    for step, state in enumerate(path, start=1):
            printState(state, step)
    #Process Heuristic 2
    startTime2 = time.time()
    for puzzle in boardStates:
        searchCost2, path = aStarSearch(puzzle,goalState, h2)
        totalCostH2 += searchCost2
    for step, state in enumerate(path, start=1):
            printState(state, step)
    endTime2 = time.time()
    runTime2 = endTime2 - startTime2

    #Print Results
    print("H1 Average Search Cost: ", totalCostH1/len(boardStates))
    print("H1 Runtime: ",round(runTime1* 1000,2), "milliseconds")
    print("H2 Average Search Cost: ", totalCostH2/len(boardStates))
    print("H2 Runtime: ",round(runTime2* 1000,2), "milliseconds")
    print("\n")     

def main():
    print("CS 4200 Project 1 by Joshua Bicera")
    print("----------------------------------")
    while True:
        print("Select:")
        print("[1] Single Test Puzzle")
        print("[2] File Input")
        print("[3] Exit")
        choice = int(input())

        if choice == 1:
            singleTestPuzzle()
        elif choice == 2:
            calcFilePuzzles()
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

main()

