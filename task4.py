import pprint
import string

assignments = []
sectionRanges = []

def CreateRanges(assignments):
    for assignment in assignments:
        sectionRanges.append(CreateRange(assignment))
    return sectionRanges

def CreateRange(assignment):
    expandedRange = []
    # turn each line into two lists
    assignmentSplit = assignment.split(',')
    for ass in assignmentSplit:
        split_ass = ass.split('-')
        new_range = list(range(int(split_ass[0]),int(split_ass[1])+1))
        expandedRange.append(new_range)
    return expandedRange

def main():
    with open('task4Input.txt', 'r') as f:
        for line in f.readlines():
            assignments.append(line.replace("\n",""))
    ranges = CreateRanges(assignments)
    count = 0
    for r in ranges:
        check =  all(item in r[0] for item in r[1])
        check2 =  all(item in r[1] for item in r[0])
        if check:
            count+=1
        elif check2:
            count+=1

    pprint.pprint(count)

if __name__ == "__main__":
    main()
