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

    input = [
        ".F----7F7F7F7F-7....",
        ".|F--7||||||||FJ....",
        ".||.FJ||||||||L7....",
        "FJL7L7LJLJ||LJ.L-7..",
        "L--J.L7...LJS7F-7L7.",
        "....F-J..F7FJ|L7L7L7",
        "....L7.F7||L7|.L7L7|",
        ".....|FJLJ|FJ|F7|.LJ",
        "....FJL-7.||.||||...",
        "....L---J.LJ.LJLJ..."
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

                x = 0

                while "FJ" in corners[x:]:
                    x = corners.find("FJ", x) + 1
                    pipes += 1

                x = 0

                while "L7" in corners[x:]:
                    x = corners.find("L7", x) + 1
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

    start.setNext(next)
    start.next.setPrevious(start)

    start.setLoop(True)
    next.setLoop(True)

    current = next

    while current != start:

        match current.id:

            case "-":
                if grid[current.y][current.x-1].loop == False:
                    next = grid[current.y][current.x-1]
                elif grid[current.y][current.x+1].loop == False:
                    next = grid[current.y][current.x+1]
                else:
                    next = start                
            case "|":
                if grid[current.y+1][current.x].loop == False:
                    next = grid[current.y+1][current.x]
                elif grid[current.y-1][current.x].loop == False: 
                    next = grid[current.y-1][current.x]
                else:
                    next = start                    
            case "7":
                if grid[current.y][current.x-1].loop == False:
                    next = grid[current.y][current.x-1]
                elif grid[current.y+1][current.x].loop == False: 
                    next = grid[current.y+1][current.x]
                else:
                    next = start
            case "F":
                if grid[current.y][current.x+1].loop == False:
                    next = grid[current.y][current.x+1]
                elif grid[current.y+1][current.x].loop == False: 
                    next = grid[current.y+1][current.x]
                else:
                    next = start                    
            case "J":
                if grid[current.y-1][current.x].loop == False:
                    next = grid[current.y-1][current.x]
                elif grid[current.y][current.x-1].loop == False: 
                    next = grid[current.y][current.x-1]
                else:
                    next = start
            case "L":
                if grid[current.y-1][current.x].loop == False:
                    next = grid[current.y-1][current.x]
                elif grid[current.y][current.x+1].loop == False: 
                    next = grid[current.y][current.x+1]     
                else:
                    next = start               
            case "S":
                print("Helllo")
                break
            case _:
                print("No no no")
                exit(-1)

        next.setPrevious(current)
        next.setLoop(True)
        current.setNext(next)

        if (next == start):
            break

        current = next
    
def traverse(start):

    left = start.previous
    right = start.next

    steps = 1

    while left != right:

        left = left.previous
        right = right.next

        steps += 1

    return steps

def pipe(begin, end):

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
    print()
    points.printgrid(grid)
    print()
    
    loop(grid, start)
    
    start.id = pipe(start.previous, start.next)
    
    enclosed(grid)    

    sum = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x].enclosed == True:
                #print(f"y: {y} x: {x}")
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