#Advent of Code 2023 Day 15

from tools import files
import time

def test():

    input = [ "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7" ]

    return input

def parse(input):
    return input[0].split(",")

def algo(label):

    out = 0
    for letter in label:
        out += ord(letter)
        out *= 17
        out = out % 256

    return out

def part1(input):

    #input = test()

    sum = 0

    steps = parse(input)
    for step in steps:
        sum += algo(step)

    print("Part 1: {}".format(sum))

def create():
    
    boxes = []
    for _ in range(256):
        boxes.append({})

    return boxes

def fill(boxes, steps):

    for step in steps:
        
        if step[-1] == "-":
            label = step[:-1]
            box = algo(label)

            if label in boxes[box]:
                temp = boxes[box]
                del temp[label]

        else:
            label, lens = step.split("=")
            lens = int(lens)
            box = algo(label)

            temp = boxes[box]
            temp[label] = lens

    return boxes

def calculate(filled):

    sum = 0

    for x, box in enumerate(filled):
        
        for y, lense in enumerate(box):
            number = x+1
            number *= (y+1)
            number *= box[lense]

            sum += number

    return sum

def part2(input):

    #input = test()
    boxes = create()

    steps = parse(input)
    filled = fill(boxes, steps)

    sum = calculate(filled)

    print("Part 2: {}".format(sum))    

filename = "input/15.txt"
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