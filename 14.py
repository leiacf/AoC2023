#Advent of Code 2023 Day 14

from tools import files
from tools import points
from functools import cache
import time

def test():

    input = [

        "O....#....",
        "O.OO#....#",
        ".....##...",
        "OO.#O....O",
        ".O.....O#.",
        "O.#..O.#.#",
        "..O..#O..O",
        ".......O..",
        "#....###..",
        "#OO..#...."

     ]

    return input

def parse(input):
    
    grid = []

    for line in input:
        grid.append(line)

    return grid

def rotate(grid):

    new = grid
  
    new = list(map(list, zip(*new)))
    for y in range(len(new)):
        line = "".join(new[y])
        new[y] = line
    
    return new

def tilt(grid):

    for y, line in enumerate(grid):

        splits = line.split("#")

        for x, split in enumerate(splits):
            split = list(split)
            split.sort(reverse=True)

            temp = "".join(split)
            splits[x] = temp

        line = "#".join(splits)
        grid[y] = line

    return grid

def reverse(grid):

    for y, line in enumerate(grid):
        line = line[::-1]
        grid[y] = line

    return grid

def cycle(grid):

    #N W S E

    #N
    grid = rotate(grid)
    grid = tilt(grid)
    grid = rotate(grid)

    #W
    grid = tilt(grid)

    #S
    grid = rotate(grid)
    grid = reverse(grid)
    grid = tilt(grid)
    grid = reverse(grid)
    grid = rotate(grid)

    #E
    grid = reverse(grid)
    grid = tilt(grid)
    grid = reverse(grid)

    return grid

def calculate(grid):

    load  = 0
    
    for line in grid:
        for x, letter in enumerate(line):

            if letter == "O":
                load += len(line)-x

    return load

def part1(input):

    #input = test()
    
    grid = parse(input)
    grid = rotate(grid)
    grid = tilt(grid)
    load = calculate(grid)

    print("Part 1: {}".format(load))

def part2(input):

    #input = test()
    grid = parse(input)

    cache = []
    start = 0
    end = 0

    for i in range(999999999):

        grid = cycle(grid)

        if grid in cache:
            end = i
            length = end - cache.index(grid)
            break

        else:
            cache.append(grid)

    times = (1000000000 - end) // length
    start = end + (times*length)

    for _ in range(start, 999999999):
        grid = cycle(grid)

    grid = rotate(grid)
    load = calculate(grid)

    print("Part 2: {}".format(load))    

filename = "input/14.txt"
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