#Advent of Code 2023 Day 17

from tools import files
from tools import points
from tools import djikstra
import time

def test():

    input = [ 
        "2413432311323",
        "3215453535623",
        "3255245654254",
        "3446585845452",
        "4546657867536",
        "1438598798454",
        "4457876987766",
        "3637877979653",
        "4654967986887",
        "4564679986453",
        "1224686865563",
        "2546548887735",
        "4322674655533"
    ]

    return input

def parse(input):

    grid = []

    for y, line in enumerate(input):
        temp = []
        for x, digit in enumerate(line):
            point = points.Point(x, y, digit)
            temp.append(point)

        grid.append(temp)

    return grid

def part1(input):

    input = test()
    grid = parse(input)
    crucible = grid[0][0]
    djikstra.djikstra(grid, crucible)

    path = grid[-1][-1].cost

    print("Part 1: {}".format(path))

def part2(input):

    input = test()

    print("Part 2: {}".format(1))    

filename = "input/17.txt"
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