import math

def splitCompartments(ruckSack):
    length = len(line)
    middle = math.floor(length / 2)
    firstPart = line[0:middle]
    secondPart = line[middle: length]
    return [firstPart, secondPart]

def findDuplicates(firstCompartment, secodCompartment):
    duplicates = set()
    for character in firstCompartment:
        if (character in secodCompartment):
            duplicates.add(character)
    return duplicates

with open('day3\puzzleInput.txt') as f:
    lines = f.readlines()
    allDuplicates = []
    for line in lines:
        line = line.replace("\n", "")
        compartments = splitCompartments(line)
        duplicates = findDuplicates(compartments[0], compartments[1])
        allDuplicates.append(duplicates)
    
    upperSubVal = 64
    total = 0
    for item in allDuplicates:
        for dup in item:
            val = 0
            converted = ord(dup)
            if dup.isupper():
                val = (converted - upperSubVal) + 26
            elif dup.islower():
                val = (converted - (upperSubVal+26+6))
            total = total + val
    print("Overall Total: " + str(total))
            
