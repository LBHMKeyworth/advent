import pprint

all_elves = []

with open('task1Input.txt', 'r') as f:
    for line in f.readlines():
        all_elves.append(line.replace("\n",""))
calories = 0
elf_totals = []
for snack in all_elves:
    if snack != "":
        calories += int(snack)
    else:
        elf_totals.append(calories)
        calories = 0


pprint.pprint(sorted(elf_totals, reverse=True)[:1])
#get top 3 elves
pprint.pprint(sorted(elf_totals, reverse=True)[:3])
pprint.pprint(sum(sorted(elf_totals, reverse=True)[:3]))
