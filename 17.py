#Advent of Code 2023 Day 17

from tools import files
from heapq import heappush, heappop
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

    heatmap = {}

    for y, line in enumerate(input):
        for x, heat in enumerate(line):
            heatmap[(x, y)] = heat

    return heatmap

def neighbours():

    n = []

    n.append(( 1, 0))
    n.append(( 0,  1))
    n.append((-1,  0))
    n.append(( 0,  -1))

    return n

def isvalid(city, coords):
    return coords in city

def pathfinder(city, start, goal):

    queue = [(0, start, (0, 0), 0)]
    visited = set()
    
    while queue:

        heat, coords, direction, steps = heappop(queue)

        if (coords, direction, steps) in visited:
            continue

        visited.add((coords, direction, steps))

        if coords == goal:
            return heat

        if steps < 3 and direction != (0,0):
            
            nex = (coords[0] + direction[0], coords[1] + direction[1])
            
            if isvalid(city, nex):
                heappush(queue, (heat + int(city[nex]), nex, direction, steps+1))

        for d in neighbours():
            neigh = (coords[0]+d[0], coords[1]+d[1])

            if isvalid(city, neigh):
                if d != direction and d != (-direction[0], -direction[1]):
                    heappush(queue, (heat + int(city[neigh]), neigh, d, 1))

    return 0

def ultra(city, start, goal):

    queue = [(0, start, (0, 0), 0)]
    visited = set()
    
    while queue:

        heat, coords, direction, steps = heappop(queue)

        if (coords, direction, steps) in visited:
            continue

        visited.add((coords, direction, steps))

        if coords == goal and steps >= 4:
            return heat

        if steps < 10 and direction != (0,0):
            
            nex = (coords[0] + direction[0], coords[1] + direction[1])
            
            if isvalid(city, nex):
                heappush(queue, (heat + int(city[nex]), nex, direction, steps+1))

        if steps >= 4 or direction == (0,0):
            for d in neighbours():
                neigh = (coords[0]+d[0], coords[1]+d[1])

                if isvalid(city, neigh):
                    if d != direction and d != (-direction[0], -direction[1]):
                        heappush(queue, (heat + int(city[neigh]), neigh, d, 1))

    return 0


def part1(input):

    #input = test()
    city = parse(input)
    start = (0,0)
    goal = (len(input[0])-1,len(input)-1)
    
    heatloss = pathfinder(city, start, goal)

    print(f"Part 1: {heatloss}")

def part2(input):

    #input = test()

    city = parse(input)
    start = (0,0)
    goal = (len(input[0])-1,len(input)-1)
    
    heatloss = ultra(city, start, goal)

    print(f"Part 2: {heatloss}")
   

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