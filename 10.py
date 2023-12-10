#Advent of Code 2023 Day 10

from tools import files
from tools import points
import time

def test():

    input = [

        ".....",
        ".S-7.",
        ".|.|.",
        ".L-J.",
        "....."
         ]
    
    input = [
        "-L|F7",
        "7S-7|",
        "L|7||",
        "-L-J|",
        "L|-JF"
        ]
    
    input = [
        "..F7.",
        ".FJ|.",
        "SJ.L7",
        "|F--J",
        "LJ..."
        ]
    
    return input

def test02():

    input = [
        "...........",
        ".S-------7.",
        ".|F-----7|.",
        ".||.....||.",
        ".||.....||.",
        ".|L-7.F-J|.",
        ".|..|.|..|.",
        ".L--J.L--J.",
        "..........."
    ]

    input = [
        "..........",
        ".S------7.",
        ".|F----7|.",
        ".||....||.",
        ".||....||.",
        ".|L-7F-J|.",
        ".|..||..|.",
        ".L--JL--J.",
        ".........."
    ]

    return input

def parse(input):

    grid = []

    for y in range(len(input)):
        temp = []
        for x in range(len(input[0])):

            point = points.Point(x, y, input[y][x])
            temp.append(point)

        grid.append(temp)

    start = None

    for pnts in grid:
        for pnt in pnts:
            if pnt.id == "S":
                start = pnt
                break

    return grid, start

def enclosed(grid):

    for y in range(len(grid)):
        for x in range(len(grid[0])):

            current = grid[y][x]
            
            if current.loop == True:
                continue

            pipes = 0
            corners = ""

            #right
            for i in range(x+1, len(grid[y])):
                test = grid[y][i]

                if test.id == "|" and test.loop == True:
                    pipes += 1

                if test.id in ["7", "F", "J", "L"] and test.loop == True:
                    corners += test.id

            if len(corners) > 0:

                if "FJ" in corners:
                    pipes += 1
                if "L7" in corners:
                    pipes += 1
                
            if pipes % 2 != 0:
                current.enclosed = True

    return

def loop(grid, start):

    next = None
    
    if grid[start.y][start.x+1].id in ["-", "7", "J"]:
        next = grid[start.y][start.x + 1]
    elif grid[start.y-1][start.x].id in [ "|", "F", "7"]:
        next = grid[start.y-1][start.x]
    elif grid[start.y][start.x-1].id in [ "-", "F", "L"]:
        next = grid[start.y][start.x-1]
    elif grid[start.y+1][start.x].id in [ "|", "L", "J"]:
        next = grid[start.y+1][start.x]

    begin = None
    end = None

    start.setNext(next)
    start.next.setPrevious(start)
    
    start.setLoop(True)
    next.setLoop(True)

    while next != start:

        id = next.id

        match id:
            case "-":
                begin = grid[next.y][next.x-1]
                end = grid[next.y][next.x+1]
            case "|":
                begin = grid[next.y+1][next.x]
                end = grid[next.y-1][next.x]
            case "7":
                begin = grid[next.y][next.x-1]
                end = grid[next.y+1][next.x]
            case "F":
                begin = grid[next.y+1][next.x]
                end = grid[next.y][next.x+1]
            case "L":
                begin = grid[next.y-1][next.x]
                end = grid[next.y][next.x+1]
            case "J":
                begin = grid[next.y-1][next.x]
                end = grid[next.y][next.x-1]
            case "S":
                break
            case _:
                print("No no no")
                exit(-1)

        previous = next

        if begin.loop == True:
            next = end
        elif end.loop == True:
            next = begin

        previous.setNext(next)
        next.setPrevious(previous)
        next.setLoop(True)
    
def traverse(start):

    begin = start.previous
    end = start.next

    steps = 1

    while begin != end:

        begin = begin.previous
        end = end.next

        steps += 1

    return steps

def pipe(begin, end):

    combo = begin.id + end.id

    if combo in ["--", "F-"]:
        return "-"
    
    return "F"

def part1(input):

    #input = test()
    grid, start = parse(input)
    
    loop(grid, start)
    max = traverse(start)

    print("Part 1: {}".format(max))

def part2(input):

    input = test02()

    grid, start = parse(input)
    points.printgrid(grid)
    loop(grid, start)
    start.id = pipe(start.previous, start.next)
    enclosed(grid)    

    sum = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x].enclosed == True:
                print(f"y: {y} x: {x}")
                sum += 1

    print("Part 2: {}".format(sum))    

filename = "input/10.txt"
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