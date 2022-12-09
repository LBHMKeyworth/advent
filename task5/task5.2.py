import pprint
import string

# [N]     [C]                 [Q]
# [W]     [J] [L]             [J] [V]
# [F]     [N] [D]     [L]     [S] [W]
# [R] [S] [F] [G]     [R]     [V] [Z]
# [Z] [G] [Q] [C]     [W] [C] [F] [G]
# [S] [Q] [V] [P] [S] [F] [D] [R] [S]
# [M] [P] [R] [Z] [P] [D] [N] [N] [M]
# [D] [W] [W] [F] [T] [H] [Z] [W] [R]
#  1   2   3   4   5   6   7   8   9


stack1 = ['D','M','S','Z','R','F','W','N']
stack2 = ['W','P','Q','G','S']
stack3 = ['W','R','V','Q','F','N','J','C']
stack4 = ['F','Z','P','C','G','D','L']
stack5 = ['T','P','S']
stack6 = ['H','D','F','W','R','L']
stack7 = ['Z','N','D','C']
stack8 = ['W','N','R','F','V','S','J','Q']
stack9 = ['R','M','S','G','Z','W','V']

movements = []

stacks = {'1': stack1, '2': stack2, '3': stack3, '4': stack4, '5': stack5, '6': stack6, '7':stack7, '8': stack8, '9':stack9}

REPLACEMENTS = [
    ("move ", ""),
    ("from ", ""),
    ("to ", ""),
]

def moveCrates(movement):
    #move 8 from 2 to 6
    #firstName, lastName = myString.split(' ', 1)

    noOfCrates, sourceStack, destinationStack = movement.split(' ')
    stacks[destinationStack].extend(stacks[sourceStack][-int(noOfCrates):])
    del stacks[sourceStack][len(stacks[sourceStack]) -int(noOfCrates):]

def main():
    with open('task5InputMovements.txt', 'r') as f:
        for line in f.readlines():
            movements.append(line.replace("\n",""))
    for movement in movements:
        for old, new in REPLACEMENTS:
            movement = movement.replace(old, new)
        moveCrates(movement)
    topOfStacks = ""
    for x in range(1, 10):
        topOfStacks += stacks[str(x)].pop()
    pprint.pprint(topOfStacks)

if __name__ == "__main__":
    main()
