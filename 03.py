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
        ".664.598.#",
        ]

    return input

def symbols(input):
    poi = []
    
    for y in range(len(input)):
        for x in range(len(input[0])):
            test = input[y][x]

            if test != "." and test != "\n" and not test.isdigit():
                
                if y > 0:
                    startY = y-1
                else:
                    startY = y

                if x > 0:
                    startX = x-1
                else:
                    startX = x

                if y < len(input)-1:
                    endY = y+1
                else:
                    endY = y

                if x < len(input[0])-1:
                    endX = x+1
                else:
                    endX = x
            
                poi.append([test, startY, endY, startX, endX])

    return poi

def digits(input):

    numbers = []

    for y in range(len(input)):
        line = input[y]
        for x in range(len(input[0])):

            if line[x].isdigit():

                num = 0
                counter = x

                if counter >= 0:
                    while line[counter].isdigit():
                        counter -= 1

                counter += 1
                start = counter

                if counter < (len(line)-1):

                    while line[counter].isdigit() and counter < len(line)-1:
                        counter += 1

                end = counter

                if (start == end):
                    num = int(line[start])

                elif (end == len(line)):
                    num = int(line[start:])

                else:
                    num = int(line[start:end])

                temp = [num, y, start, end]

                if temp not in numbers:
                    numbers.append(temp)

    return numbers

def check(poi, numbers):

    valid = []

    for number, y, start, end in numbers:

        for symbol, startY, endY, startX, endX in poi:

            if y in range(startY, endY+1):
                found = False

                if (start == end):
                    if start in range(startX, endX+1):
                        valid.append(number)
                        found = True
                        break

                for z in range(start, end):

                    if z in range(startX, endX+1):

                        valid.append(number)
                        found = True
                        break
                    
                if found:
                    break

    return valid

def parse(input):

    poi = symbols(input)
    numbers = digits(input)

    valid = check(poi, numbers)

    sum = 0

    for number in valid:
        sum += number

    return sum

def part1(input):

    input = test()
    sum = parse(input)

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