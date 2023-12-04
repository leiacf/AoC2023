#Advent of Code 2023 Day XX

from tools import files
import time

def test():

    input = [ ]

    return input

def part1(input):

    #input = test()

    print("Part 1: {}".format(1))

def part2(input):

    #input = test()

    print("Part 2: {}".format(1))    

filename = "input/XX.txt"
#input = files.input_as_list(filename)

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