import pprint


#A = Rock
#B = Paper
#C = Scissors
#X = lose
#Y = draw
#Z = win
#Rock = 1
#Paper = 2
#Scissors = 3

result = {"AX" : 3, # = lose = scissors = 3 + 0
           "AY" : 1 + 3, # = draw = rock = 1+3
           "AZ" : 2 + 6, # = win = paper = 2+6
           "BX" : 1 + 0, # = lose = rock = 1 + 0
           "BY" : 2 + 3, # = draw = paper = 2 + 3
           "BZ" : 3 + 6, # = win = scissors = 3 + 6
           "CX" : 2, # = lose = paper = 2 + 0
           "CY" : 3 + 3, # = draw = scissors = 3 + 3
           "CZ" : 1 + 6, # = win = rock = 1 + 6
}

all_rounds = []



def play_round(round):
    return result[round]

def main():
    total_score = 0
    with open('task2Input.txt', 'r') as f:
        for line in f.readlines():
            all_rounds.append(line.replace("\n","").replace(" ",""))
    for round in all_rounds:
        total_score += play_round(round)

    pprint.pprint(total_score)

if __name__ == "__main__":
    main()
