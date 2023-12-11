#Advent of Code 2023 Day 11

from tools import files
from tools import points
import time

def test():

    input = [ 
        "...#......",
        ".......#..",
        "#.........",
        "..........",
        "......#...",
        ".#........",
        ".........#",
        "..........",
        ".......#..",
        "#...#....."
    ]

    return input

def expand(input, amount):
    
    expanded = []

    #rows
    for line in input:

        expanded.append(line)
        if not "#" in line:
            for i in range(1, amount):
                expanded.append(line)

    col = []

    #columns
    for x in range(len(expanded[0])):
        found = False
        for y in range(len(expanded)):
            if expanded[y][x] == "#":
                found = True
                break
        if found == False:
            col.append(x)

    col.sort(reverse = True)

    for x in col:
        for y in range(len(expanded)):
            line = expanded[y]
            new = line[:x+1]
            new += "." * (amount-1)
            new += line[x+1:]
            expanded[y] = new

    return expanded

def parse(expanded):

    grid = []

    for y in range(len(expanded)):
        temp = []
        for x in range(len(expanded[y])):
            point = points.Point(x, y, expanded[y][x])
            temp.append(point)
        grid.append(temp)

    return grid

def galaxies(grid):

    gal = []

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x].id == "#":
                gal.append(grid[y][x])

    return gal

def part1(input):

    input = test()

    expanded = expand(input, 2)
    grid = parse(expanded)

    gal = galaxies(grid)

    distances = []

    for i in range(len(gal)):
        for j in range(i+1, len(gal)):
            dist = points.calculate_manhattan([gal[i].y, gal[i].x], [gal[j].y, gal[j].x])
            distances.append(dist)

    sum = 0

    for i in distances:
        sum += i

    print("Part 1: {}".format(sum))

def amounts(grid):

    row = []

    for y in range(len(grid)):
        found = False
        for x in range(len(grid[y])):
            if grid[y][x].id == "#":
                found = True
                break
        if found == False:
            row.append(y)

    col = []

    for x in range(len(grid[0])):
        found = False
        for y in range(len(grid)):
            if grid[y][x].id == "#":
                found = True
                break
        if found == False:
            col.append(x)

    col.sort(reverse = True)

    return row, col

def calculate(row, col, gal, amount):

    distances = []

    for i in range(len(gal)):
        for j in range(i+1, len(gal)):

            ys = [min(gal[i].y, gal[j].y), max(gal[i].y, gal[j].y)]
            xs = [min(gal[i].x, gal[j].x), max(gal[i].x, gal[j].x)]
            
            county = 0
            countx = 0

            for y in row:
                if y in range(ys[0], ys[1]+1):
                    county += 1
            
            for x in col:
                if x in range(xs[0], xs[1]+1):
                    countx += 1

            sidex=1
            sidey=1

            if gal[i].x > gal[j].x:
                sidex = -1
            
            if gal[i].y > gal[j].y:
                sidey = -1

            dist = points.calculate_manhattan( [gal[i].y, gal[i].x], [ gal[j].y +( county * (amount-1) * sidey) , gal[j].x + ( countx *  (amount-1) * sidex) ] )
            distances.append(dist)

    sum = 0

    for dist in distances:
        sum += dist

    return sum

def part2(input):

    #input = test()

    grid = parse(input)
    gal = galaxies(grid)
    row, col = find(grid)

    sum = calculate(row, col, gal, 1000000)
    
    print("Part 2: {}".format(sum))    

filename = "input/11.txt"
input = files.input_as_list(filename)

print()

start1 = time.perf_counter()
part1(input)
end1 = time.perf_counter()

start2 = time.perf_counter()
part2(input)
end2 = time.perf_counter()

print()
print("Spent {:>7.2f} seconds on Part 1".format(end1-start1))
print("Spent {:>7.2f} seconds on Part 2".format(end2-start2))