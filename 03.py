#Advent of Code 2023 Day 03

from tools import files
import time

def test():
    input = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598.."
    ]

    return input

def parse(input):

    numbers = []

    for _ in range(len(input)):
        numbers.append([False for x in range(len(input[0]))])

    for y in range(len(input)):
        for x in range(len(input[0])):

            if input[y][x].isdigit():

                if x > 0:
                    if input[y][x-1] != "." and not input[y][x-1].isdigit():
                            numbers[y][x] = True

                    if y < len(input)-1:
                        if input[y+1][x-1] != "." and not input[y+1][x-1].isdigit():
                            numbers[y][x] = True

                    if y > 0:

                        if input[y-1][x-1] != "." and not input[y-1][x-1].isdigit():
                            numbers[y][x] = True

                if y > 0:
                     
                    if input[y-1][x] != "." and not input[y-1][x].isdigit():
                            numbers[y][x] = True

                    if y < len(input)-1:
                        if input[y+1][x] != "." and not input[y+1][x].isdigit():
                            numbers[y][x] = True

                if x < len(input[0])-1:

                    if input[y][x+1] != "." and not input[y][x+1].isdigit():
                            numbers[y][x] = True                 
                                                
                    if y < len(input)-1:
                        if input[y-1][x+1] != "." and not input[y-1][x+1].isdigit():
                            numbers[y][x] = True

                        if input[y+1][x+1] != "." and not input[y+1][x+1].isdigit():
                            numbers[y][x] = True

    return numbers

def show(numbers):
     
    for y in range(len(numbers)):
        for x in range(len(input[0])):
             print(numbers[y][x], end="")
             print(" ", end="")
        print()

def find(numbers, input):

    sum = 0
    last = ""
    where = 0
     
    for y in range(len(numbers)):

        for x in range(len(numbers[0])):

            if numbers[y][x] == True:
                line = input[y]
                counter = x

                if counter > 0:
                    while line[counter].isdigit():
                        counter -= 1

                start = counter
                counter += 1

                if counter < (len(line)-1):

                    while line[counter].isdigit() and counter < len(line)-1:
                        counter += 1

                end = counter

                if end == len(line):
                    num = int(line[start+1:])
                else:
                    num = int(line[start+1:end])
                
                if num != last:
                    sum += num

                elif (num == last):
                    if x > where+1:
                        sum += num
                
                last = num
                where = x

    return sum

def part1(input):

    #input = test()
    numbers = parse(input)

    sum = find(numbers, input)

    print("Part 1: {}".format(sum))

def part2(input):

    print("Part 2: {}".format(1))    

filename = "input/03.txt"
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