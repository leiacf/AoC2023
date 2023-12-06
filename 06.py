#Advent of Code 2023 Day 06

from tools import files
import time

def test():

    input = [
        "Time:      7  15   30",
        "Distance:  9  40  200"
     ]

    return input

def parse(input):

    races = []
    line = input[0]
    line = line[line.find(":")+1:]
    line = line.strip()
    
    times = [int(a) for a in line.split()]
    line = input[1]
    line = line[line.find(":")+1:]
    line = line.strip()
    
    dist = [int(a) for a in line.split()]

    for x in range(len(times)):
        races.append([times[x], dist[x]])

    return races

def win(speed, time, dist):

    return speed*time > dist

def push(races):
    
    total = 1

    for time, dist in races:

        wins = 0

        for button in range(time):
            if win(button, time-button, dist):
                wins += 1

        total *= wins

    return total

def fix(races):

    race = []

    total = ""
    distance = ""

    for time, dist in races:

        total += str(time)
        distance += str(dist)

    race.append([int(total), int(distance)])

    return race

def part1(input):

    #input = test()

    races = parse(input)
    total = push(races)

    print("Part 1: {}".format(total))

def part2(input):

    #input = test()

    races = parse(input)
    race = fix(races)
    total = push(race)

    print("Part 2: {}".format(total))    

filename = "input/06.txt"
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