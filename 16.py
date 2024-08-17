#Advent of Code 2023 Day 16

from tools import files
from tools import tiles
import sys
import time

def test():

    input = [ 
        ".|...\....",
        "|.-.\.....",
        ".....|-...",
        "........|.",
        "..........",
        ".........\\",
        "..../.\\\\..",
        ".-.-/..|..",
        ".|....-|.\\",
        "..//.|....",
    ]

    return input

def parse(input):

    grid = []
    for y, line in enumerate(input):
        temp = []
        for x, letter in enumerate(line):
            tile = tiles.Tile(x, y, letter)
            temp.append(tile)

        grid.append(temp)

    return grid

def flow(grid, beam):

    x = beam.x
    y = beam.y

    if (x < 0 or x >= len(grid[0])) or (y < 0 or y >= len(grid)):
        return

    match beam.id:
        case ">":

            if grid[y][x].id == ">":
                return

            if grid[y][x].id in ".^<v":
                grid[y][x].id = beam.id
                beam.x += 1

            elif grid[y][x].id == "\\":
                beam.id = "v"
                beam.y += 1

            elif grid[y][x].id == "/":
                beam.id = "^"
                beam.y -= 1

            elif grid[y][x].id == "|": 
                split = tiles.Tile(x, y-1, "^")
                flow(grid, split)
                beam.id = "v"
                beam.y += 1

            elif grid[y][x].id == "-":
                beam.x += 1

        case "v":

            if grid[y][x].id == "v":
                return

            if grid[y][x].id in ".^<>":
                grid[y][x].id = beam.id
                beam.y += 1

            elif grid[y][x].id == "\\":
                beam.id = ">"
                beam.x += 1

            elif grid[y][x].id == "/":
                beam.id = "<"
                beam.x -= 1

            elif grid[y][x].id == "|": 
                beam.y += 1

            elif grid[y][x].id == "-":
                split = tiles.Tile(x-1, y, "<")
                flow(grid, split)
                beam.id = ">"
                beam.x += 1
                
        case "<":

            if grid[y][x].id == "<":
                return

            if grid[y][x].id in ".^>v":
                grid[y][x].id = beam.id
                beam.x -= 1

            elif grid[y][x].id == "\\":
                beam.id = "^"
                beam.y -= 1

            elif grid[y][x].id == "/":
                beam.id = "v"
                beam.y += 1

            elif grid[y][x].id == "|": 
                split = tiles.Tile(x, y-1, "^")
                flow(grid, split)
                beam.id = "v"
                beam.y += 1

            elif grid[y][x].id == "-":
                beam.x -= 1

        case "^":

            if grid[y][x].id == "^":
                return
            
            if grid[y][x].id in ".><v":
                grid[y][x].id = beam.id
                beam.y -= 1

            elif grid[y][x].id == "\\":
                beam.id = "<"
                beam.x -= 1

            elif grid[y][x].id == "/":
                beam.id = ">"
                beam.x += 1

            elif grid[y][x].id == "|": 
                beam.y -= 1

            elif grid[y][x].id == "-":
                split = tiles.Tile(x-1, y, "<")
                flow(grid, split)
                beam.id = ">"
                beam.x += 1

    grid[y][x].beams += 1

    flow(grid, beam)

def calculate(grid, beam):

    flow(grid, beam)

    sum = 0

    for line in grid:
        for point in line:
            if point.beams > 1 and point.id in ".^v<>":
                point.id = str(point.beams)

    for line in grid:
        for point in line:
            if point.beams > 0:
                sum += 1
    
    return sum

def part1(input):

    #input = test()
    grid = parse(input)
    beam = tiles.Tile(0, 0, ">")
    
    sys.setrecursionlimit(2100)

    sum = calculate(grid, beam)

    print("Part 1: {}".format(sum))

def part2(input):

    #input = test()
    grid = parse(input)
    energy = []

    sys.setrecursionlimit(2900)

    for x in range(len(grid[0])):
        
        grid = parse(input)
        beam = tiles.Tile(x, 0, "v")
        
        sum = calculate(grid, beam)
        energy.append(sum)
    
    for x in range(len(grid[0])):
        
        grid = parse(input)
        beam = tiles.Tile(x, len(grid)-1, "^")
        
        sum = calculate(grid, beam)
        energy.append(sum)

    for y in range(len(grid)):
        
        grid = parse(input)
        beam = tiles.Tile(0, y, ">")
        
        sum = calculate(grid, beam)
        energy.append(sum)

    for y in range(len(grid)):
        
        grid = parse(input)
        beam = tiles.Tile(len(grid[0])-1, y, "<")

        sum = calculate(grid, beam)
        energy.append(sum)        

    energy.sort(reverse=True)

    print("Part 2: {}".format(energy[0]))

filename = "input/16.txt"
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