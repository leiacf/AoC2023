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

    input = [
        "FF7FSF7F7F7F7F7F---7",
        "L|LJ||||||||||||F--J",
        "FL-7LJLJ||||||LJL-77",
        "F--JF--7||LJLJ7F7FJ-",
        "L---JF-JLJ.||-FJLJJ7",
        "|F|F-JF---7F7-L7L|7|",
        "|FFJF7L7F-JF7|JL---7",
        "7-L-JL7||F7|L7F-7F7|",
        "L.L7LFJ|||||FJL7||LJ",
        "L7JLJL-JLJLJL--JLJ.L"
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

            for i in range(x+1, len(grid[y])):
                test = grid[y][i]

                if test.id in ["|", "L", "J"] and test.loop == True:
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
                break
            case _:
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

def pipe(previous, next):

    id = None

    match previous.id:

        case "-":

            if next.y == previous.y:
                id = "-"

            elif next.y < previous.y:
                if next.x < previous.x:
                    id = "7"
                elif next.x > previous.x:
                    id = "F"

            elif next.y > previous.y:
                if next.x < previous.x:
                    id = "J"
                elif next.x > previous.x:
                    id = "L"
        case "|":

            if next.x == previous.x:
                id = "|"

            elif next.x < previous.x:
                if next.y < previous.y:
                    id = "7"
                elif next.y > previous.y:
                    id = "J"

            elif next.x > previous.x:
                if next.y < previous.y:
                    id = "F"
                elif next.y > previous.y:
                    id = "L"

        case "7":
            
            if next.x == previous.x:
                id = "|"
            
            if next.x < previous.x:
                if next.y == previous.y:
                    id = "-"
                elif next.y < previous.y:
                    id = "L"
                elif next.y > previous.y:
                    id = "F"
            
            if next.x > previous.x:
                if next.y > previous.y:
                    id = "L"
        case "F":
            
            if next.x == previous.x:
                id = "|"
            
            if next.x < previous.x:
                if next.y > previous.y:
                    id = "J"
            
            if next.x > previous.x:
                if next.y == previous.y:
                    id = "-"
                elif next.y < previous.y:
                    id = "J"
                elif next.y > previous.y:
                    id = "7"

        case "J":
            
            if next.x == previous.x:
                id = "|"
            
            if next.x < previous.x:
                if next.y == previous.y:
                    id == "-"
                elif next.y < previous.y:
                    id = "L"
                elif next.y > previous.y:
                    id = "F"
            
            if next.x > previous.x:
                if next.y < previous.y:
                    id = "F"

        case "L":

            if next.x == previous.x:
                id = "|"
            
            if next.x < previous.x:
                if next.y < previous.y:
                    id = "7"
            
            if next.x > previous.x:
                if next.y == previous.y:
                    id = "-"
                if next.y < previous.y:
                    id = "J"
                if next.y > previous.y:
                    id = "7"

        case _:
            exit(-1)

    return id

def part1(input):

    #input = test()
    grid, start = parse(input)
    
    loop(grid, start)
    max = traverse(start)

    print("Part 1: {}".format(max))

def part2(input):

    #input = test02()

    grid, start = parse(input)
    loop(grid, start)
    start.id = pipe(start.previous, start.next)
    
    enclosed(grid)    

    sum = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x].enclosed == True:
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