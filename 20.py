#Advent of Code 2023 Day 20

from tools import files
from tools import modules as m
import time
import queue
import math

def test():

    input = [
        "broadcaster -> a, b, c",
        "%a -> b",
        "%b -> c",
        "%c -> inv",
        "&inv -> a"
     ]

    return input

def test2():

    input = [

        "broadcaster -> a",
        "%a -> inv, con",
        "&inv -> b",
        "%b -> con",
        "&con -> output"

    ]

    return input

def parse(input):

    modules = []
    button = None
    output = None

    for line in input:
        name, outputs = line.split(" -> ")

        if name[0] == "%":
            typ = name[0]
            name = name[1:]
            temp = m.Flip(name, typ, outputs)

        elif name[0] == "&":
            typ = name[0]
            name = name[1:]
            temp = m.Con(name, typ, outputs)

        else:
            typ = name
            temp = m.Module(name, typ, outputs)

        modules.append(temp)

        if name == "broadcaster":
            button = m.Module("button", "button", temp)
            temp.setInput(button)

    for module in modules:
        outputs = module.outputs

        if outputs != [None]:
            splits = outputs[0].split(", ")

            temp = []

            for split in splits:
                found = False
                for mod in modules:
                    if mod.name == split:
                        temp.append(mod)
                        mod.setInput(module)
                        found = True
                if not found:
                    output = m.Module(split, split, None)
                    output.setInput(module)
                    temp.append(output)
                    modules.append(output)

                module.outputs = temp

    for module in modules:
        if isinstance(module, m.Con):
            module.initInputs()

    return button, modules, output

def simulate(button, modules, high, low):

    broadcaster = None

    for module in modules:
        if module.name == "broadcaster":
            broadcaster = module
            break

    order = queue.Queue()
    order.put((0, button, broadcaster))
    low += 1

    while not order.empty():

        pulse, fro, to = order.get()

        send, outputs = to.get(pulse, fro)

        if send != None and outputs != [None]:

            for o in outputs:
                order.put((send, to, o))
                if send == 1:
                    high += 1
                elif send == 0:
                    low += 1

    return high, low

def pulse(button, modules, amounts, x):

    broadcaster = None

    for module in modules:
        if module.name == "broadcaster":
            broadcaster = module
            break

    order = queue.Queue()
    order.put((0, button, broadcaster))

    while not order.empty():

        pulse, fro, to = order.get()

        send, outputs = to.get(pulse, fro)

        if send != None and outputs != [None]:

            for o in outputs:
                order.put((send, to, o))
                if send == 1 and to in amounts.keys() and amounts[to] == 0:
                    amounts[to] = x+1

def part1(input):
    
    #input = test2()

    button, modules, _ = parse(input)
    
    high = 0
    low = 0

    for _ in range(1000):
        high, low = simulate(button, modules, high, low)

    print(f"Part 1: {low*high}")

def part2(input):

    #input = test()

    button, modules, output = parse(input)

    inputs = output.inputs[0].inputs
    amounts = {}

    for i in inputs:
        amounts[i] = 0

    for x in range(5000):
        pulse(button, modules, amounts, x)

    values = []

    for v in amounts.values():
        values.append(v)

    presses = math.lcm(*values)

    print("Part 2: {}".format(presses))    

filename = "input/20.txt"
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