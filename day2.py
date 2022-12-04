
def part1():
    lookup = {
    #   rock    paper   scizzers
        "X": 1, "Y": 2, "Z": 3,
        "A": 1, "B": 2, "C": 3 
    } 

    with open('input/02', 'r') as file:
        totalScore = 0
        for line in file:
            x = line.split()
            if lookup[x[0]] == lookup[x[1]]:
                totalScore += 3
            elif x[1] == 'X' and x[0] == 'C':
                totalScore += 6
            elif x[1] == 'Y' and x[0] == 'A':
                totalScore += 6
            elif x[1] == 'Z' and x[0] == 'B':
                totalScore += 6
            totalScore += lookup[x[1]]
    print(totalScore)
    
    
def part2():
    lookup = {
    #   rock    paper   scizzers
        "X": 1, "Y": 2, "Z": 3,
        "A": 1, "B": 2, "C": 3 
        }
    totalScore = 0
    with open('input/02', 'r') as file:
        for line in file:
            x = line.split()
            if x[1] == "Y":
                totalScore += lookup[x[0]] + 3 
            elif x[1] == "X":
                if x[0] == 'A':
                    totalScore += lookup["Z"]
                elif x[0] == 'B':
                    totalScore += lookup["X"]
                else:
                    totalScore += lookup["Y"]
            else:
                totalScore += 6
                if x[0] == 'A':
                    totalScore += lookup["Y"]
                elif x[0] == 'B':
                    totalScore += lookup["Z"] 
                else:
                    totalScore += lookup["X"] 
    print(totalScore)
    
part2()