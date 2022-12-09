import pprint
import string

rucksacks = []

common = []

priorities = {}

def getPriority(letter):
    return priorities[letter]

def buildPriorities():
    letters = []
    letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    number = 1
    for letter in letters:
        priorities[letter] = number
        number = number + 1


def main():
    buildPriorities()
    total = 0
    with open('task3Input.txt', 'r') as f:
        for line in f.readlines():
            rucksacks.append(line.replace("\n",""))
    for compartment in rucksacks:
        #split strings in half
        compartment1 = slice(0,len(compartment)//2)
        compartment2 = slice(len(compartment)//2, len(compartment))
        #get common elements in two lists
        common = list(set(compartment[compartment1]) & set(compartment[compartment2]))
        for letter in common:
            total = total + getPriority(letter)
    pprint.pprint(total)

if __name__ == "__main__":
    main()
