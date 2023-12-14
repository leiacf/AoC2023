#Advent of Code 2023 Day 13

from tools import files
from tools import points
import time

def test():

    input = [ 

        "#.##..##.",
        "..#.##.#.",
        "##......#",
        "##......#",
        "..#.##.#.",
        "..##..##.",
        "#.#.##.#.",
        "",
        "#...##..#",
        "#....#..#",
        "..##..###",
        "#####.##.",
        "#####.##.",
        "..##..###",
        "#....#..#",
        ""

    ]

    return input

def parse(input):

    grids = []
    grid = []

    for line in input:
        if line == "":
            grids.append(grid)
            grid = []
        else:
            grid.append(line)

    return grids

def convert(grid):

    converted = []

    for x in range(len(grid[0])):
        line = ""
        for y in range(len(grid)):
            line += grid[y][x]
        converted.append(line)

    return converted

def mirror(grid):

    above = 0

    for y in range(len(grid)):

        found = False
        down = y-1

        for up in range(y, len(grid)):

            if down == -1:
                break

            one = grid[down]
            two = grid[up]

            if one == two:
                down -= 1
                found = True
                continue
            else:
                found = False
                break

        if found == True:
            above = y
            return above

    return above

def mirror_persist(grid, last):

    above = 0

    for y in range(len(grid)):

        found = False
        down = y-1

        for up in range(y, len(grid)):

            if down == -1:
                break

            one = grid[down]
            two = grid[up]

            if one == two:
                down -= 1
                found = True
                continue
            else:
                found = False
                break

        if found == True:
            if y == last:
                found = False
                continue
            else:
                above = y
            return above

    return above

def check(grid):

    above = 0
    left = 0

    # horizontal
    above = mirror(grid)

    # vertical
    if above == 0:
        hor = convert(grid)
        left = mirror(hor)

    return above, left

def check_persist(grid, last):

    above = 0
    left = 0

    # horizontal
    above = mirror_persist(grid, last)

    # vertical
    if above == 0:
        hor = convert(grid)
        left = mirror_persist(hor, last)

    return above, left

def calculate(grid):
    
    above, left = check(grid)
    total = left + (above*100)

    return total

def calculate_persists(grid, last):
    
    above, left = check_persist(grid, last)
    total = left + (above*100)

    return total

def reflect(grids):

    total = 0
    
    for grid in grids:
        total += calculate(grid)

    return total

def change(grid, x, y):

    new = []

    for line in grid:
        new.append(line)

    line = new[y]

    if line[x] == ".":
        line = line[:x] + "#" + line[x+1:]
    else:
        line = line[:x] + "." + line[x+1:]

    new[y] = line

    return new

def smudge(grids):

    total = 0
    matches = 0

    for grid in grids:

        found = False

        for y in range(len(grid)):
            for x in range(len(grid[0])):

                last = max(check(grid))

                new = change(grid, x, y)

                if check(grid) != check_persist(new, last):
                    if ((0, 0) != check_persist(new, last)):

                        matches += 1
                        total += calculate_persists(new, last)
                        found = True
                        break

            if found:
                break

        if not found:
            points.printgrid(grid)

    print(f"Found {matches} matches for {len(grids)} grids")

    print()

    print("Off by one grid error. Probably because the persist functions doesn't take above and left into account, need to persist both")
    print("Manually solved for now (counting the rows to the the smudge for the missing grid and calculating by hand)")

    print()

    return total

def part1(input):

    #input = test()
    grids = parse(input)
    total = reflect(grids)

    print(f"Part 1: {total}")

def part2(input):

    #input = test()
    grids = parse(input)
    total = smudge(grids)

    print(f"Part 2: {total}")    

filename = "input/13.txt"
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