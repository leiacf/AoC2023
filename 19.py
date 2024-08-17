#Advent of Code 2023 Day 19

from tools import files
import time
import copy

def test():

    input = [

        "px{a<2006:qkq,m>2090:A,rfg}",
        "pv{a>1716:R,A}",
        "lnx{m>1548:A,A}",
        "rfg{s<537:gd,x>2440:R,A}",
        "qs{s>3448:A,lnx}",
        "qkq{x<1416:A,crn}",
        "crn{x>2662:A,R}",
        "in{s<1351:px,qqz}",
        "qqz{s>2770:qs,m<1801:hdj,R}",
        "gd{a>3333:R,R}",
        "hdj{m>838:A,pv}",
        "",
        "{x=787,m=2655,a=1222,s=2876}",
        "{x=1679,m=44,a=2067,s=496}",
        "{x=2036,m=264,a=79,s=2244}",
        "{x=2461,m=1339,a=466,s=291}",
        "{x=2127,m=1623,a=2188,s=1013}"

     ]

    return input

def parse(input):

    rules = {}
    parts = []

    for line in input:

        if line == "":
            continue

        if line[0] == "{":

            temp = {}

            line = line.replace("{", "")
            line = line.replace("}", "")

            splits = line.split(",")
            
            for split in splits:
                letter, number = split.split("=")
                number = int(number)
                temp[letter] = number

            parts.append(temp)

        else:
            
            name, rule = line.split("{")
            rule = rule.replace("}", "")

            splits = rule.split(",")
            rules[name] = splits

    return rules, parts

def follow(rules, part, name, rejected, accepted):

    rule = rules[name]

    conditions = rule[:-1]
    final = rule[-1]

    for condition in conditions:

        test, destination = condition.split(":")

        letter = test[0]
        check = test[1]
        number = int(test[2:])

        matched = False

        match check:
            case "<":
                if part[letter] < number:
                    matched = True
            case ">":
                if part[letter] > number:
                    matched = True

        if matched:         

            if destination == "R":
                if part not in rejected:
                    rejected.append(part)
                    return
            elif destination == "A":
                if part not in accepted:
                    accepted.append(part)
                    return
            else:
                follow(rules, part, destination, rejected, accepted)
                return


    if final == "R":
        if part not in rejected:
            rejected.append(part)
            return
    elif final == "A":
        if part not in accepted:
            accepted.append(part)
            return
    else:
        follow(rules, part, final, rejected, accepted)
        return
    
def recursive(rules, xmas, name, accepted):

    rule = rules[name]

    conditions = rule[:-1]
    final = rule[-1]

    for condition in conditions:

        test, destination = condition.split(":")

        letter = test[0]
        check = test[1]
        number = int(test[2:])

        lower, upper = xmas[letter]

        if check == "<":

            if lower >= number:
                continue

            if upper < number:
                recursive(rules, xmas, destination, accepted)
                return

            matched = copy.deepcopy(xmas)

            l = (lower, number-1)
            u = (number, upper)

            matched[letter] = l
            xmas[letter] = u

            if destination == "R":
                pass
            elif destination == "A":
                accepted.append(matched)
            else:
                recursive(rules, matched, destination, accepted)

        elif check == ">":

            if upper <= number:
                continue

            if lower > number:
                recursive(rules, xmas, destination, accepted)
                return
            
            matched = copy.deepcopy(xmas)

            l = (lower, number)
            u = (number+1, upper)

            matched[letter] = u
            xmas[letter] = l

            if destination == "R":
                pass       
            elif destination == "A":
                accepted.append(matched)
            else:
                recursive(rules, matched, destination, accepted)

    if final == "R":
        pass
    elif final == "A":
        accepted.append(xmas)
    else:
        recursive(rules, xmas, final, accepted)

def calculate(rules):

    combinations = 0
    accepted = []
    
    xmas = {}

    #initial ranges
    xmas["x"] = (1,4000)
    xmas["m"] = (1,4000)
    xmas["a"] = (1,4000)
    xmas["s"] = (1,4000)

    recursive(rules, xmas, "in", accepted)

    for parts in accepted:
        temp = 1
        for lower, upper in parts.values():
            temp *= (upper+1-lower)

        combinations += temp
    
    return combinations

def part1(input):

    rejected = []
    accepted = []

    #input = test()

    rules, parts = parse(input)

    for part in parts:
        follow(rules, part, "in", rejected, accepted)

    sum = 0

    for part in accepted:
        rating = 0

        for value in part.values():
            rating += value

        sum += rating

    print(f"Part 1: {sum}")

def part2(input):

    #input = test()

    rules, _ = parse(input)
    
    sum = calculate(rules)

    print(f"Part 2: {sum}")    

filename = "input/19.txt"
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