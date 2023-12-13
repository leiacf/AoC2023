#Advent of Code 2023 Day 12
#Finally solved part 2, but by looking at what others have done
#Trying hard to learn, NOT to just blindly copy code
#Learned: Dynamic programming, what types of problems it can be used on, memoization

from tools import files
import time

def test():

    input = [

        "#.#.### 1,1,3",
        ".#...#....###. 1,1,3",
        ".#.###.#.###### 1,3,1,6",
        "####.#...#... 4,1,1",
        "#....######..#####. 1,6,5",
        ".###.##....# 3,2,1"

        ]
    
    input = [

        "???.### 1,1,3",
        ".??..??...?##. 1,1,3",
        "?#?#?#?#?#?#?#? 1,3,1,6",
        "????.#...#... 4,1,1",
        "????.######..#####. 1,6,5",
        "?###???????? 3,2,1",

    ]    

    return input

def parse(input):

    data = []

    for line in input:
        springs, groups = line.split()
        groups = [int(a) for a in groups.split(",")]
        data.append([springs, groups])

    return data

def expand(input):

    expanded = []

    for line in input:
        
        springs, numbers = line.split(" ")

        one = "?".join((springs,) * 5)
        two = ",".join((numbers,) * 5 )

        expanded.append(one+ " " + two)
        
    return expanded

dp = {}
def dynamic(springs, groups, index, groupindex, hashes):
   
    state = (index, groupindex, hashes)

    if state in dp:
        return dp[state]

    # exit conditions (end of the line)
    if index == len(springs):

        # At the end of the line, no more groups and no hashes
        # Nothing left to check - So there's exactly 1 valid combination
        if groupindex == len(groups) and hashes == 0:
            return 1
        # At the end of a line, and still in the last group with hashes checked
        # If everything matches, there's exactly 1 valid combination
        elif groupindex == len(groups)-1 and groups[groupindex] == hashes:
            return 1
        # At the end of a line, but something isn't right
        # Has to be invalid, so returning 0
        else:
            return 0

    total = 0

    # For every index, do the following checks for both .'s and #'s
    for character in ".#":
        
        # Treating question marks as the same character that is currently checked (thus ensuring all combinations are looked at)
        if springs[index] == character or springs[index] == "?":

            # Recursive combinations that affect the total score
            if character == "." and hashes==0:
                # Not in a run at all! 
                # Moving to the next index, keeping the group index stable because it wasn't matched yet, still have no hashes
                total += dynamic(springs, groups, index+1, groupindex, 0)

            elif character == "." and hashes > 0 and groupindex < len(groups) and groups[groupindex] == hashes:
                # Just finished a run, it matches what was expected! 
                # Moving to the next index, moving to the next run, resetting hashcount
                total += dynamic(springs, groups, index+1, groupindex+1, 0)

            elif character == "#":
                # In the middle of an unfinished run!
                #  Moving to the next index, keeping the group index stable because it wasn't matched yet, counting another hash
                total += dynamic(springs, groups, index+1, groupindex, hashes+1)

    dp[state] = total 

    return total

def part1(input):

    #input = test()
    data = parse(input)
    
    total = 0

    for springs, groups in data:
        dp.clear()
        total += dynamic(springs, groups, 0, 0, 0)

    print(f"Part 1: {total}")

def part2(input):

    #input = test()
    expanded = expand(input)
    data = parse(expanded)

    total = 0

    for springs, groups in data:
        dp.clear()
        total += dynamic(springs, groups, 0, 0, 0)
    
    print(f"Part 2: {total}")    

filename = "input/12.txt"
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