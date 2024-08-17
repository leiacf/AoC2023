import math

class Point:

    def __init__(self, x, y, id=""):

        self.x = x
        self.y = y
        self.id = id
        self.visited = False
        self.cost = math.inf
        self.loop = False
        self.next = None
        self.previous = None
        self.enclosed = False

    def __str__(self):
        return self.id
    
    def setCost(self, cost):
        self.cost = cost

    def setVisited(self, bool):
        self.visited = bool

    def setLoop(self, bool):
        self.loop = bool

    def setNext(self, next):
        self.next = next

    def setPrevious(self, previous):
        self.previous = previous

    def setEnclosed(self, bool):
        self.enclosed = bool

def calculate_manhattan(p, q):
    return ( abs(p[0]-q[0]) + abs(p[1]-q[1]) )

def grid(width, height):
        
    grid = []

    for y in range(height):
        line = []
        for x in range(width):
            line.append(".")
        grid.append(line)
    
    return grid

def printgrid(grid):

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            print(grid[y][x], end="")
        print()

def printgridcost(grid):

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x].cost == math.inf:
                print(" ", end="")
            else:
                print(grid[y][x].cost, end="")

        print()

def printgridloop(grid):

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x].loop == False:
                print(".", end="")
            else: 
                print("T", end="")
        print()

def printgridenclosed(grid):

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x].enclosed == False:
                print(".", end="")
            else:
                print("T", end="")
        print()