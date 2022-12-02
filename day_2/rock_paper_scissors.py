with open("input.txt") as file:
    input_txt = file.readlines()
    for i in range(len(input_txt)):
        input_txt[i] = input_txt[i].split()


def solution_1():
    class Round:
        def __init__(self, elf, me):
            self.elf = elf
            self.me = me

        def score(self):
            score = 0

            match self.me:
                case "X":
                    score += 1

                case "Y":
                    score += 2

                case "Z":
                    score += 3

            if (self.elf == "A" and self.me == "Y") or (self.elf == "B" and self.me == "Z") or (
                    self.elf == "C" and self.me == "X"):
                score += 6

            elif (self.elf == "A" and self.me == "X") or (self.elf == "B" and self.me == "Y") or (
                    self.elf == "C" and self.me == "Z"):
                score += 3

            else:
                score += 0

            return score

    score = 0

    for i in range(len(input_txt)):
        single_round = Round(input_txt[i][0], input_txt[i][1])
        score += single_round.score()

    print(score)


def solution_2():
    class Round:
        def __init__(self, elf, outcome):
            self.elf = elf
            self.outcome = outcome

        def score(self):
            score = 0

            match self.outcome:
                case "X":
                    score += 0

                    if self.elf == "A":
                        score += 3

                    elif self.elf == "B":
                        score += 1

                    elif self.elf == "C":
                        score += 2

                case "Y":
                    score += 3

                    if self.elf == "A":
                        score += 1

                    elif self.elf == "B":
                        score += 2

                    elif self.elf == "C":
                        score += 3

                case "Z":
                    score += 6

                    if self.elf == "A":
                        score += 2

                    elif self.elf == "B":
                        score += 3

                    elif self.elf == "C":
                        score += 1

            return score

    score = 0

    for i in range(len(input_txt)):
        single_round = Round(input_txt[i][0], input_txt[i][1])
        score += single_round.score()

    print(score)


solution_2()
