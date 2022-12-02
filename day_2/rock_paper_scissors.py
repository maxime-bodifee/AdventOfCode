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
            score_total = 0

            match self.me:
                case "X":
                    score_total += 1

                case "Y":
                    score_total += 2

                case "Z":
                    score_total += 3

            if (self.elf == "A" and self.me == "Y") or (self.elf == "B" and self.me == "Z") or (
                    self.elf == "C" and self.me == "X"):
                score_total += 6

            elif (self.elf == "A" and self.me == "X") or (self.elf == "B" and self.me == "Y") or (
                    self.elf == "C" and self.me == "Z"):
                score_total += 3

            else:
                score_total += 0

            return score_total

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
            score_total = 0

            match self.outcome:
                case "X":
                    score_total += 0

                    if self.elf == "A":
                        score_total += 3

                    elif self.elf == "B":
                        score_total += 1

                    elif self.elf == "C":
                        score_total += 2

                case "Y":
                    score_total += 3

                    if self.elf == "A":
                        score_total += 1

                    elif self.elf == "B":
                        score_total += 2

                    elif self.elf == "C":
                        score_total += 3

                case "Z":
                    score_total += 6

                    if self.elf == "A":
                        score_total += 2

                    elif self.elf == "B":
                        score_total += 3

                    elif self.elf == "C":
                        score_total += 1

            return score_total

    score = 0

    for i in range(len(input_txt)):
        single_round = Round(input_txt[i][0], input_txt[i][1])
        score += single_round.score()

    print(score)


solution_2()
