#Advent of Code 2023 Day 01

from tools import files
import time

def test():

    input = {
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    }

    return input

def findNumbers(line):

    where = {}
    
    numbers = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
    
    for number in numbers:
        temp = []

        if number in line:
            first = line.find(number)
            last = line.rfind(number)    
            
            if first == last:
                temp.append(first)

            else:
                temp.append(first)
                temp.append(last)
                        
        if len(temp) > 0:
            where[number] = temp

    return where

def replace(line, where):

    if len(where) == 0:
        return line

    numbers = {
                "one": "1", 
                "two": "2", 
                "three": "3", 
                "four": "4", 
                "five": "5", 
                "six": "6", 
                "seven": "7", 
                "eight": "8", 
                "nine": "9", 
               }
    
    for number, loc in where.items():

        for i in loc:
            line = line[:i] + numbers[number] + line[i+1:]

    return line

def part1(input):

    digits = []

    for line in input:
        temp = []
        for letter in line:
            if  letter.isdigit():
                temp.append(letter)

        digits.append(temp)

    sum = 0

    for row in digits:
        num = row[0] + row[-1]
        sum += int(num)

    print("Part 1: {}".format(sum))

def part2(input):

    #input = test()
    new = []

    for line in input:

        numbers = findNumbers(line)
        line = replace(line, numbers)

        new.append(line)

    digits = []

    for line in new:
        temp = []

        for letter in line:
            if letter.isdigit():
                temp.append(letter)

        digits.append(temp)

    sum = 0

    for row in digits:
        num = row[0] + row[-1]
        sum += int(num)

    print("Part 2: {}".format(sum))    

filename = "input/01.txt"
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