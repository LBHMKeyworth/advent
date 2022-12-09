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
    i = 1

    groups = [rucksacks[x:x+3] for x in range(0, len(rucksacks), 3)]
    for group in groups:
        commonItem = list(set(group[0]) & set(group[1]) & set(group[2]))
        #pprint.pprint(commonItem)
        total = total + getPriority(commonItem[0])
    pprint.pprint(total)

if __name__ == "__main__":
    main()
