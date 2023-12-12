#Advent of Code 2023 Day 12

from tools import files
import time

def test():

    input = [

        "#.#.### 1,1,3",
        ".#...#....###. 1,1,3",
        ".#.###.#.###### 1,3,1,6",
        "####.#...#... 4,1,1",
        "#....######..#####. 1,6,5",
        ".###.##....# 3,2,1",

     ]
    
    input = [

        "???.### 1,1,3",
        ".??..??...?##. 1,1,3",
        "?#?#?#?#?#?#?#? 1,3,1,6",
        "????.#...#... 4,1,1",
        "????.######..#####. 1,6,5",
        "?###???????? 3,2,1",

    ]

    return input

def parse(input):

    everything = {}

    for line in input:
        springs, groups = line.split()
        groups = [int(a) for a in groups.split(",")]
        everything[springs] = groups

    return everything

def unknowns(split):
    return "?" in split

def divide(split):

    design = []
    count = 1

    for x in range(len(split)-1):

        if split[x] == split[x + 1]:
            count += 1
        else:
            design.append(count)
            count = 1
    
    design.append(count)

    return design

def arrange(springs, groups):

    arrange = 0

    if "?" in springs:

        splits = list(filter(None, springs.split(".")))
        arrangements = 0

    return arrange


def calculate(everything):

    arr = []

    for springs, groups in everything.items():
        
        if "?" not in springs:
            arrangements = 1
        else:
            arrangements = arrange(springs, groups)

        arr.append([springs, groups, arrangements])

    return arr

def part1(input):

    input = test()

    everything = parse(input)
    arr = calculate(everything)

    sum = 0

    for x in range(len(arr)):
        sum += arr[x][2]


    print("Part 1: {}".format(sum))

def part2(input):

    #input = test()

    print("Part 2: {}".format(1))    

filename = "input/12.txt"
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