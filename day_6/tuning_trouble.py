with open("input.txt") as file:
    input_txt = file.readline().strip("\n")

with open("example.txt") as file:
    input_txt_example = file.readline().strip("\n")


def solution_1(input_txt):
    for i in range(len(input_txt)):
        if len(set(input_txt[i:i+4])) == 4:
            print(i + 4)
            break


def solution_2(input_txt):
    for i in range(len(input_txt)):
        if len(set(input_txt[i:i+14])) == 14:
            print(i + 14)
            break


solution_2(input_txt)
