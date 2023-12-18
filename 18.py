#Advent of Code 2023 Day 18

from tools import files
from tools import points
import time

def test():

    input = [ 

        "R 6 (#70c710)",
        "D 5 (#0dc571)",
        "L 2 (#5713f0)",
        "D 2 (#d2c081)",
        "R 2 (#59c680)",
        "D 2 (#411b91)",
        "L 5 (#8ceee2)",
        "U 2 (#caa173)",
        "L 1 (#1b58a2)",
        "U 2 (#caa171)",
        "R 2 (#7807d2)",
        "U 3 (#a77fa3)",
        "L 2 (#015232)",
        "U 2 (#7a21e3)"

    ]

    return input

def parse(input):

    instructions = []

    for line in input:
        temp = line.split(" ")
        temp[1] = int(temp[1])
        instructions.append(temp)

    return instructions

def corners(instructions):

    digger = (0, 0)
    lagoon = []

    lagoon.append(digger)

    for direction, length, _ in instructions:

        match direction:

            case "U":
                digger = (digger[0]-length, digger[1])
            case "R":
                digger = (digger[0], digger[1]+length)
            case "D":
                digger = (digger[0]+length, digger[1])
            case "L":
                digger = (digger[0], digger[1]-length)

        if digger not in lagoon:
            lagoon.append(digger)

    lagoon.append((0, 0))

    return lagoon

def shoelace(vertices):

    result = 0

    vertices.reverse()

    for i in range(len(vertices)-1):

        y1, x1 = vertices[i]
        y2, x2 = vertices[i+1]
    
        result += x1*y2 - x2*y1

    result = abs(result) // 2
    
    return result

def pick(interior, vertices):

    boundry = 0

    for i in range(len(vertices)-1):

        y1, x1 = vertices[i]
        y2, x2 = vertices[i+1]
    
        boundry += points.calculate_manhattan((y1, x1), (y2,x2))

    area = interior - (boundry // 2) + 1

    return area + boundry

def calculate(vertices):

    result = shoelace(vertices)
    amount = pick(result, vertices)

    return amount

def convert(input):

    converted = []

    for line in input:
        _, _, instruction = line.split(" ")

        instruction = instruction.replace("(#", "")
        instruction = instruction.replace(")", "")

        direction = instruction[-1:]

        if direction == "0":
            direction = "R"
        elif direction == "1":
            direction = "D"
        elif direction == "2":
            direction = "L"
        elif direction == "3":
            direction = "U"

        length = int(instruction[:-1], 16)

        temp = direction + " " + str(length) + " " + "_"
        converted.append(temp)

    return converted

def part1(input):

    #input = test()
    instructions = parse(input)

    vertices = corners(instructions)
    amount = calculate(vertices)
    
    print(f"Part 1: {amount}")

def part2(input):

    #input = test()

    converted = convert(input)
    instructions = parse(converted)

    vertices = corners(instructions)
    amount = calculate(vertices)

    print(f"Part 2: {amount}")    

filename = "input/18.txt"
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