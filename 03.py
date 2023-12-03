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
        ".664.598..",
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

                if x < len(input[y])-1:
                    endX = x+1
                else:
                    endX = x
            
                poi.append([test, startY, endY, startX, endX])

    #for line in poi:
    #    print(line)

    return poi

def digits(input):

    numbers = []

    for y in range(len(input)):

        line = input[y]
        
        for letter in range(len(line)):

            if line[letter].isdigit():
                
                start = letter

                if letter > 0:
                    while start > -1 and line[start].isdigit():
                        start -= 1
                    start += 1

                end = letter

                if end < len(line):

                    while end < len(line) and line[end].isdigit():
                        end += 1
                    end -= 1

                num = int(line[start:end+1])

                temp = [num, y, start, end]

                if temp not in numbers:
                    numbers.append(temp)

    #for line in numbers:
    #    print(line)

    return numbers

def check(poi, numbers):

    valid = []

    for number, y, start, end in numbers:

        for _, startY, endY, startX, endX in poi:

            if y not in range(startY, endY+1):
                continue

            found = False

            for z in range(start, end+1):

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

def gears(input):

    poi = symbols(input)
    numbers = digits(input)

    sum = 0

    for symbol, startY, endY, startX, endX in poi:

        adjacent = []

        if symbol != "*":
            continue

        for number, y, start, end in numbers:

            if y not in range(startY, endY+1):
                continue

            for z in range(start, end+1):

                if z in range(startX, endX+1):
                    adjacent.append(number)
                    break

        if len(adjacent) == 2:
            sum += (adjacent[0] * adjacent[1])

    return sum

def part1(input):

    #input = test()
    sum = parse(input)

    print("Part 1: {}".format(sum))

def part2(input):

    #input = test()
    sum = gears(input)

    print("Part 2: {}".format(sum))    

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