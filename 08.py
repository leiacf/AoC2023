#Advent of Code 2023 Day 08

from tools import files
from tools import nodes as n
import time
import math

def test():

    input = [
        "RL",
        "",
        "AAA = (BBB, CCC)",
        "BBB = (DDD, EEE)",
        "CCC = (ZZZ, GGG)",
        "DDD = (DDD, DDD)",
        "EEE = (EEE, EEE)",
        "GGG = (GGG, GGG)",
        "ZZZ = (ZZZ, ZZZ)"
     ]
    
    return input

def test02():
    
    input = [
        "LR",
        "",
        "11A = (11B, XXX)",
        "11B = (XXX, 11Z)",
        "11Z = (11B, XXX)",
        "22A = (22B, XXX)",
        "22B = (22C, 22C)",
        "22C = (22Z, 22Z)",
        "22Z = (22B, 22B)",
        "XXX = (XXX, XXX)"
    ]

    return input

def parse(input):
    instructions = input[0]
    nodes = []

    for line in input[2:]:
        line = line.replace("= (", "")
        line = line.replace (")", "")
        line = line.replace(",", "")

        split = line.split(" ")
        name = split[0]
        children = [split[1], split[2]]

        node = n.Node(name, children)
        nodes.append(node)

    for node in nodes:
        for x in range(len(node.children)):
            child = node.children[x]
            for nod in nodes:
                if nod.name == child:
                    child = nod
                node.children[x] = child

    return instructions, nodes

def cycle(instructions, nodes):

    start = []

    for node in nodes:
        if node.name[-1] == "A":
            start.append(node)
    
    cyc = []
    
    for node in start:

        steps = 0
        next = node

        while True:
            
            found = False
            
            for ins in instructions:
                if ins == "R":
                    next = next.children[1]
                else:
                    next = next.children[0]

                steps += 1

                if next.name[-1] == "Z":
                    stop = next
                    found = True
                    break

            if found:
                cyc.append([node, stop, steps])
                break
    
        if len(cyc) == len(start):
            break
    
    cycs = []
    
    for line in cyc:
        cycs.append(line[2])

    total = math.lcm(*(cycs))

    return total

def part1(input):

    #input = test()

    next = ""
    instructions, nodes = parse(input)
    
    for node in nodes:
        if node.name == "AAA":
            next = node
            break
    
    steps = 0
    found = False

    while True:

        for ins in instructions:

            if (ins) == "R":
                next = next.children[1]
            elif (ins) == "L":
                next = next.children[0]
            
            steps += 1

            if next.name == "ZZZ":
                found = True
                break
        
        if found:
            break             

    print("Part 1: {}".format(steps))

def part2(input):

    # input = test02()

    instructions, nodes = parse(input)

    total = cycle(instructions, nodes)

    print("Part 2: {}".format(total))    

filename = "input/08.txt"
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