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
        ".###.##....# 3,2,1"

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

    data = []

    for line in input:
        springs, groups = line.split()
        groups = [int(a) for a in groups.split(",")]
        data.append([springs, groups])

    return data

def is_valid(springs, groups):

    lengths = []
    splits = list(filter(None, springs.split(".")))

    for split in splits:
        lengths.append(len(split))
    
    return lengths == groups

def expand(input):

    expanded = []

    for line in input:
        
        springs, numbers = line.split(" ")

        one = "?".join((springs,) * 5)
        two = ",".join((numbers,) * 5 )

        expanded.append(one+ " " + two)
        
    return expanded

def recursive(springs, groups):

    if "?" not in springs:
        if is_valid(springs, groups):
            return 1
        
    else:

        for x, letter in enumerate(springs):
        
            if letter == "?":

                first = springs[:x] + "." + springs[x+1:]
                second = springs[:x] + "#" + springs[x+1:]

                one = recursive(first, groups)
                two = recursive(second, groups)

                return one+two

    return 0
    
def calculate(data):

    arrangements = []

    for springs, groups in data:
        total = recursive(springs, groups)
        arrangements.append([springs, groups, total])

    return arrangements

def part1(input):

    #input = test()

    data = parse(input)
    arr = calculate(data)

    sum = 0

    for x in range(len(arr)):
        sum += arr[x][2]

    print("Part 1: {}".format(sum))

def part2(input):

    input = test()
    expanded = expand(input)

    data = parse(expanded)
    arr = calculate(data)

    sum = 0

    for x in range(len(arr)):
        sum += arr[x][2]
        print(x)

    print("Part 2: {}".format(sum))    

filename = "input/12.txt"
input = files.input_as_list(filename)

print()

start1 = time.perf_counter()
part1(input)
end1 = time.perf_counter()

start2 = time.perf_counter()
#part2(input)
end2 = time.perf_counter()

print()
print("Spent {:>7.2f} seconds on Part 1".format(end1-start1))
print("Spent {:>7.2f} seconds on Part 2".format(end2-start2))