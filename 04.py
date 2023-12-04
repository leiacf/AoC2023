#Advent of Code 2023 Day 04

from tools import files
import time

def test():

    input = [ 
"Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
"Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
"Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
"Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
"Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
"Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"

    ]

    return input

def parse(input):

    cards = []

    for line in input:
        line = line.replace("Card ", "")
        index = line.find(":")
        line = line[index+1:]

        winning, numbers = line.split("|")

        winning = winning.replace("  ", " ")
        numbers = numbers.replace("  ", " ")

        winning = winning.strip()
        numbers = numbers.strip()

        cards.append((winning, numbers))

    return cards

def multiply(cards):
    
    copies = {}

    for x, card in enumerate(cards):

        winning = card[0]
        numbers = card[1]

        won = 0

        w = [int(a) for a in winning.split(" ")]
        n = [int(b) for b in numbers.split(" ")]

        for y in n:
            if y in w:           
                won += 1

        if card in copies:
            have = copies[card]+1
        else:
            have = 1

        for _ in range(have):        

            for i in range(x+1, x+won+1):

                if i < len(cards):
                
                    if cards[i] in copies:
                        copies[cards[i]] += 1
                    else:
                        copies[cards[i]] = 1

    return copies

def part1(input):

    #input = test()
    cards = parse(input)

    sum = 0

    for winning, numbers in cards:

        points = 0
        won = 0

        w = [int(a) for a in winning.split(" ")]
        n = [int(b) for b in numbers.split(" ")]

        for x in n:
            if x in w:           
                won += 1
                if won == 1:
                    points = 1
                else:
                    points *= 2

        sum += points

    print("Part 1: {}".format(sum))

def part2(input):

    #input = test()
    cards = parse(input)
    copies = multiply(cards)

    sum = 0

    for card in cards:

        amount = 1

        if card in copies:
            amount += copies[card]

        sum += amount

    print("Part 2: {}".format(sum))    

filename = "input/04.txt"
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