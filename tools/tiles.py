class Tile:

    def __init__(self, x, y, id="", beams=0):

        self.x = x
        self.y = y
        self.id = id
        self.beams = beams

    def __str__(self):
        return self.id

def printgrid(grid):

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            print(grid[y][x], end="")
        print()