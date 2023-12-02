#Advent of Code 2023 Day 02

from tools import files
import time
import math

def test():

    input = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
        ]

    return input

def parse(input):

    games = []

    for line in input:
        split = line.split(":")
        temp = {}

        for game in split:

            if ";" in game:
                game = game.strip()
                rounds = game.split("; ")

                for round in rounds:
                    cubes = round.split(", ")

                    for cube in cubes:
                        number, color = cube.split(" ")
                        number = int(number)

                        if color not in temp:
                            temp[color] = number
                        elif temp[color] <= number:
                            temp[color] = number
            else:
               game = game.replace("Game ", "")
               temp["game"] = int(game)

            if (len(temp) > 1):
                games.append(temp)

    return games

def part1(input):

    #input = test()
    check = {"red": 12, "green": 13, "blue": 14}

    games = parse(input)

    sum = 0

    for game in games:

        if game["red"] <= check["red"] and game["blue"] <= check["blue"] and game["green"] <= check["green"]:
                sum += game["game"]

    print("Part 1: {}".format(sum))

def part2(input):

    #input = test()
    games = parse(input)

    sum = 0

    for game in games:

        temp = game["red"] * game["blue"] * game["green"]
        sum += temp

    print("Part 2: {}".format(sum))    

filename = "input/02.txt"
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