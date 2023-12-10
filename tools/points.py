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

def neighbours8(x, y, maxX=None, maxY=None):

    neighbours = [
        (x-1, y-1), (x, y-1), (x+1, y-1),
        (x-1, y), (x+1, y),
        (x-1, y+1), (x, y+1), (x+1, y+1)
        ]

    if maxX != None and maxY != None:

        neighbours = []

        if x in range(0, maxX) and y in range(0, maxY):

            if y > 0:
                if x > 0:
                    neighbours.append((x-1, y-1))
                else:
                    pass
                neighbours.append((x, y-1))
                if x < maxX-1:
                    neighbours.append((x+1, y-1))
                else:
                    pass

            if x > 0:
                neighbours.append((x-1, y))
            else:
                pass
            if x < maxX-1:
                neighbours.append((x+1, y))
            else:
                pass

            if y < maxY-1:

                if x > 0:
                    neighbours.append((x-1, y+1))
                else:
                    pass
                neighbours.append((x, y+1))
                if x < maxX-1:
                    neighbours.append((x+1, y+1))
                else:
                    pass
        
    return neighbours

def neighbours4(x, y, maxX=None, maxY=None):

    neighbours = [ (x, y-1), (x+1, y), (x, y+1), (x-1, y) ]

    if maxX != None and maxY != None:

        neighbours = []

        if x in range(0, maxX) and y in range(0, maxY):

            if y > 0 and y < maxY-1:
                neighbours.append((x, y-1))
            if x < maxX-1:
                neighbours.append((x+1, y))
            if y < maxY-1:
                neighbours.append((x, y+1))
            if x > 0:
                neighbours.append((x-1, y))

    return neighbours

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