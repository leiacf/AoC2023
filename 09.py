#Advent of Code 2023 Day 09

from tools import files
import time

def test():

    input = [ 
        "0 3 6 9 12 15",
        "1 3 6 10 15 21",
        "10 13 16 21 30 45"
    ]

    return input

def parse(input):

    numbers = []

    for line in input:
        nums = [int(a) for a in line.split(" ")]
        numbers.append(nums)

    return numbers

def calculate(values):

    diffs = []

    for x in range(1, len(values)):
        diff = values[x] - values[x-1]
        diffs.append(diff)

    if all(i == 0 for i in diffs):
        values.append(values[-1] + diffs[-1])
        return values
    else:
        extra = calculate(diffs)
        values.append(values[-1] + extra[-1])
        return values

def calculate_backwards(values):

    diffs = []

    for x in range(1, len(values)):
        diff = values[x] - values[x-1]
        diffs.append(diff)

    if all(i == 0 for i in diffs):
        values.insert(0, values[0] - diffs[0])
        return values
    else:
        extra = calculate_backwards(diffs)
        values.insert(0, values[0] - extra[0])
        return values

def part1(input):

    #input = test()
    numbers = parse(input)
    sum = 0
    
    for values in numbers:
        extra = calculate(values)
        sum += extra[-1]

    print("Part 1: {}".format(sum))

def part2(input):

    #input = test()
    numbers = parse(input)
    sum = 0

    for values in numbers:
        extra = calculate_backwards(values)
        sum += extra[0]

    print("Part 2: {}".format(sum))    

filename = "input/09.txt"
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