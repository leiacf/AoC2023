import math

def djikstra(grid, start):

    visited = []
    unvisited = [start]
    start.setCost(0)
    start.setVisited(False)

    grid[start.y][start.x] = start

    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x].space == "#":
                grid[y][x].setVisited(True)
    
    while len(unvisited) != 0:

        check = unvisited.pop(0)
        check.setVisited(True)
        distance = check.cost + 1

        x = check.x
        y = check.y

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

    grid[y][x].setCost(distance)
    grid[y][x].setVisited(True)