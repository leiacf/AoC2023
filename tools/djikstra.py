import math

def djikstra(grid, start):

    left = grid[start.y][start.x+1]
    down = grid[start.y+1][start.x]

    visited = []
    unvisited = [left, down]

    left.cost = int(left.id)
    down.cost = int(down.id)

    while len(unvisited) != 0:

        check = unvisited.pop(0)
        check.setVisited(True)
        distance = check.cost + 1

        x = check.x
        y = check.y

        # TODO:
        # Find valid unvisited nodes
        # Can't move more than 3 in one direction
        # Can only turn left or right, not back -> Covered by visited?

        if x > 0:
            if grid[y][x-1].visited == False:
                    update(grid, x-1, y, distance)
                    unvisited.append(grid[y][x-1])

        if x < len(grid[0]) - 1:
            if grid[y][x+1].visited == False:
                update(grid, x+1, y, distance)
                unvisited.append(grid[y][x+1])

        if y > 0:
            if grid[y-1][x].visited == False:
                update(grid, x, y-1, distance)
                unvisited.append(grid[y-1][x])
                
        if y < len(grid) - 1:
            if grid[y+1][x].visited == False:
                update(grid, x, y+1, distance)
                unvisited.append(grid[y+1][x])

        visited.append(check)

def update(grid, x, y, distance):

    grid[y][x].setCost(distance+int(grid[y][x].id))
    grid[y][x].setVisited(True)