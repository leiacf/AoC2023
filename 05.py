#Advent of Code 2023 Day 05

from tools import files
import time
import math

def create(input):

    seeds       = []
    soilmap     = []
    fermap      = []
    watermap    = []
    lightmap    = []
    tempmap     = []
    hummap      = []
    locmap      = []

    map = []
    
    for line in input:

        if line == "":
            continue

        if "seeds" in line:
            seeds = [int(a) for a in line[line.find(":")+1:].strip().split(" ")]
            continue

        if "to-soil" in line:
            map = soilmap
            continue
        elif "to-fertilizer" in line: 
            map = fermap
            continue
        elif "to-water" in line: 
            map = watermap
            continue
        elif "to-light" in line:
            map = lightmap
            continue
        elif "to-temperature" in line:
            map = tempmap
            continue
        elif "to-humidity" in line:
            map = hummap
            continue
        elif "to-location" in line:
            map = locmap
            continue

        map.append([int(a) for a in line.strip().split(" ")])

    return seeds, soilmap, fermap, watermap, lightmap, tempmap, hummap, locmap   

def check(mapp, value):

    for destination, source, length in mapp:

        if source < value < source+length:
            value = value + (destination-source)
            break

    return value

def checkRange(mapp, start, end):

    ranges = []
    to = [[start, end]]
    i = 0

    while i < len(to):

        start = to[i][0]
        end = to[i][1]

        for destination, source, length in mapp:

            if start < end <= source or source+length <= start < end:
                continue

            elif source <= start < end <= source+length:

                begin   = start + (destination-source)
                stop    = end + (destination-source)

                start = end
                ranges.append([begin, stop])

                return ranges

            elif start < source <= end <= source+length:
                
                begin = destination
                stop = end + (destination-source)
            
                ranges.append([begin, stop])

                end = source-1

            elif source <= start <= source+length < end:
            
                begin = start + (destination-source)
                stop = source+length + (destination-source)

                ranges.append([begin, stop])
            
                start = source+length+1
            
            elif start < source < source+length < end:

                #print(f"hit! start: {start} source: {source} len: {source+length} end: {end}")
            
                ranges.append([destination, destination+length])

                start1 = start
                end1 = source-1

                start2 = source+length+1
                end2 = end

                to.append([start1, end1])
                to.append([start2, end2])

        ranges.append([start, end])

        i += 1

    return ranges

def expand(seeds):

    new = []

    for x in range(0, len(seeds), 2):

        num = seeds[0+x]
        rng = seeds[1+x]

        new.append([num, num+rng])

    return new

def parse(input):

    seeds, soilmap, fermap, watermap, lightmap, tempmap, hummap, locmap = create(input)

    small = math.inf

    for seed in seeds:

        seed = check(soilmap, seed)
        seed = check(fermap, seed)
        seed = check(watermap, seed)
        seed = check(lightmap, seed)
        seed = check(tempmap, seed)
        seed = check(hummap, seed)
        seed = check(locmap, seed)

        if seed < small:
            small = seed

    return small

def parse_again(input):

    seeds, soilmap, fermap, watermap, lightmap, tempmap, hummap, locmap = create(input)
    seeds = expand(seeds)

    soils = []
    fers = []
    waters = []
    lights = []
    temps = []
    hums = []
    locs = []
    
    for start, end in seeds:
        #print(f"checking: {start} {end}")
        soil = checkRange(soilmap, start, end)
        soils += soil

    #print(soils)

    print("fer")

    for start, end in soils:
        #print(f"checking: {start} {end}")
        #print(fermap)
        fer = checkRange(fermap, start, end)
        fers += fer

    print("water")

    for start, end in fers:
        #print(f"checking: {start} {end}")
        #print(watermap)
        water = checkRange(watermap, start, end)
        waters += water

    print("light")

    for start, end in waters:
        #print(f"checking: {start} {end}")
        #print(lightmap)
        light = checkRange(lightmap, start, end)
        lights += light

    print("temp")

    for start, end in lights:
        #print(f"checking: {start} {end}")
        #print(tempmap)
        temp = checkRange(tempmap, start, end)
        temps += temp
        #print(temps)

    print("hums")

    for start, end in temps:
        #print(f"checking: {start} {end}")
        hum = checkRange(hummap, start, end)
        hums += hum

    print("locs")

    for start, end in hums:
        #print(f"checking: {start} {end}")
        loc = checkRange(locmap, start, end)
        locs += loc
   
    #print(locs)
    print("final")

    smallest = math.inf

    for start, end in locs:
        if start < smallest:
            smallest = start
            print(smallest)

    return smallest

def part1(input):

    small = parse(input)
    print("Part 1: {}".format(small))

def part2(input):
    
    small = parse_again(input)
    #small = min(locations)

    print("Part 2: {}".format(small))    

filename = "input/05.txt"
#filename = "input/05-test.txt"
input = files.input_as_list(filename)

print()

start1 = time.perf_counter()
part1(input)
end1 = time.perf_counter()

start2 = time.perf_counter()
part2(input)
end2 = time.perf_counter()

print()
print("Spent {:>7.3f} seconds on Part 1".format(end1-start1))
print("Spent {:>7.3f} seconds on Part 2".format(end2-start2))