import math

class Point:

    def __init__(self, x, y, space):

        self.x = x
        self.y = y
        self.space = space
        self.visited = False
        self.cost = math.inf

    def __str__(self):
        return self.space
    
    def setCost(self, cost):
        self.cost = cost

    def setVisited(self, bool):
        self.visited = bool

def calculate_manhattan(p, q):
    return ( abs(p[0]-q[0]) + abs(p[1]-q[1]) )