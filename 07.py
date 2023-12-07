#Advent of Code 2023 Day 07

from tools import files
import time

class Hand():

    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = int(bid)
        self.type = self.find_type()

    def __str__(self):
        string = f"hand: {self.hand} bid: {self.bid} type: {self.type} "
        return string

    def find_type(self):

        cards = self.count()

        for value in cards.values():

            match value:
                case 5:
                    return "Five of a kind"
                case 4:
                    return "Four of a kind"
                case 3:
                    if len(cards) == 2:
                        return "Full house"
                    else:
                        return "Three of a kind"
                case 2:
                    if len(cards) == 3:
                        return "Two pairs"
                    else:
                        return "One pair"
                case 1:
                    return "High card"                    
                case _:
                    print("Huh, this should not happen")

    def change_type(self):
        if not "J" in self.hand:
            return

        j = 0

        for letter in self.hand:
            if letter == "J":
                j += 1

        match self.type:
            case "Four of a kind":
                if j == 1 or j == 4:
                    self.type = "Five of a kind"
            case "Full house":
                if j == 2 or j == 3:
                    self.type = "Five of a kind"
            case "Three of a kind":
                if j == 1 or j == 3:
                    self.type = "Four of a kind"
            case "Two pairs":
                if j == 2:
                    self.type = "Four of a kind"
                if j == 1:
                    self.type = "Full house"
            case "One pair":
                if j == 1 or j == 2:
                    self.type = "Three of a kind"
            case "High card":
                if j == 1:
                    self.type = "One pair"

    def change_digit(self):
        self.hand = self.hand.replace("J", "1")

    def count(self):

        cards = {}

        for card in self.hand:
            if card in cards:
                cards[card] += 1
            else:
                cards[card] = 1

        cards = dict(sorted(cards.items(), key=lambda item: item[1], reverse=True))

        return cards

def test():

    input = [ 
        "32T3K 765",
        "T55J5 684",
        "KTJJT 220",
        "KK677 28",
        "QQQJA 483",
    ]

    return input

def translate(card):

    digits = []

    for letter in card.hand:
        
        if not letter.isdigit():
            match letter:
                case "A":
                    digits.append(14)
                case "K":
                    digits.append(13)
                case "Q":
                    digits.append(12)
                case "J":
                    digits.append(11)
                case "T":
                    digits.append(10)
        else:
            digits.append(int(letter))
    
    return digits

def order(cards):

    translated = []

    for card in cards:
        temp = translate(card)
        translated.append([temp, card])

    translated.sort(key=lambda trans: trans[0])

    return translated

def parse(input):

    hands = []

    for line in input:
        hand, bid = line.split(" ")
        temp = Hand(hand, bid)
        hands.append(temp)

    return hands

def rank(hands):

    types = {}
    
    for hand in hands:

        if hand.type not in types:
            types[hand.type] = [hand]
        else:
            types[hand.type].append(hand)

    final = []

    if "High card" in types:
        cards = types["High card"]
        rank = order(cards)
        final += rank

    if "One pair" in types:
        cards = types["One pair"]
        rank = order(cards)
        final += rank

    if "Two pairs" in types:
        cards = types["Two pairs"]
        rank = order(cards)
        final += rank

    if "Three of a kind" in types:
        cards = types["Three of a kind"]
        rank = order(cards)
        final += rank

    if "Full house" in types:
        cards = types["Full house"]
        rank = order(cards)
        final += rank  

    if "Four of a kind" in types:
        cards = types["Four of a kind"]
        rank = order(cards)
        final += rank

    if "Five of a kind" in types:
        cards = types["Five of a kind"]
        rank = order(cards)
        final += rank

    return final

def calculate(ranked):
    
    rank = 1
    sum = 0

    for hand in ranked:
        #print(hand[1], end="")
        #print(f" {rank}")
        sum += hand[1].bid * rank
        rank += 1

    return sum

def part1(input):

    #input = test()

    hands = parse(input)
    ranked = rank(hands)
    
    sum = calculate(ranked)

    print("Part 1: {}".format(sum))

def part2(input):

    #input = test()

    hands = parse(input)
    
    for hand in hands:
        hand.change_type()
        hand.change_digit()

    ranked = rank(hands)
    
    sum = calculate(ranked)

    print("Part 2: {}".format(sum))    

filename = "input/07.txt"
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