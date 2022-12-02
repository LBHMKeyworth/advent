import pprint


#A = Rock
#B = Paper
#C = Scissors
#X = Rock = 1
#Y = Paper = 2
#Z = Scissors = 3

result = {"AX" : 1 + 3,
           "AY" : 2 + 6,
           "AZ" : 3 + 0,
           "BX" : 1 + 0,
           "BY" : 2 + 3,
           "BZ" : 3 + 6,
           "CX" : 1 + 6,
           "CY" : 2 + 0,
           "CZ" : 3 + 3,
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
