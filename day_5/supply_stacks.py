with open("input.txt") as file:
    input_txt = file.readlines()
    for i in range(10, len(input_txt)):
        input_txt[i] = input_txt[i].strip("move \n").split(" from ")
        input_txt[i][1] = input_txt[i][1].strip().split(" to ")

with open("example.txt") as file:
    input_txt_example = file.readlines()
    for i in range(5, len(input_txt_example)):
        input_txt_example[i] = input_txt_example[i].strip("move \n").split(" from ")
        input_txt_example[i][1] = input_txt_example[i][1].strip().split(" to ")

crate_stacks = [
    ["N", "B", "D", "T", "V", "G", "Z", "J"],
    ["S", "R", "M", "D", "W", "P", "F"],
    ["V", "C", "R", "S", "Z"],
    ["R", "T", "J", "Z", "P", "H", "G"],
    ["T", "C", "J", "N", "D", "Z", "Q", "F"],
    ["N", "V", "P", "W", "G", "S", "F", "M"],
    ["G", "C", "V", "B", "P", "Q"],
    ["Z", "B", "P", "N"],
    ["W", "P", "J"]
]

crate_stacks_example = [
    ["Z", "N"],
    ["M", "C", "D"],
    ["P"]
]


def answer(crate_stacks):
    answer = ""
    for i in range(len(crate_stacks)):
        answer += crate_stacks[i][-1]

    return answer


def solution_1():
    for i in range(10, len(input_txt)):
        quantity = int(input_txt[i][0])
        position_1 = int(input_txt[i][1][0]) - 1
        position_2 = int(input_txt[i][1][1]) - 1

        for _ in range(quantity):
            crate_stacks[position_2].extend(crate_stacks[position_1][-1])
            crate_stacks[position_1].pop()

    print(answer(crate_stacks))


def solution_1_example():
    for i in range(5, len(input_txt_example)):
        quantity = int(input_txt_example[i][0])
        position_1 = int(input_txt_example[i][1][0]) - 1
        position_2 = int(input_txt_example[i][1][1]) - 1

        for _ in range(quantity):
            crate_stacks_example[position_2].extend(crate_stacks_example[position_1][-1])
            crate_stacks_example[position_1].pop()

    print(answer(crate_stacks_example))


def solution_2():
    for i in range(10, len(input_txt)):
        quantity = int(input_txt[i][0])
        position_1 = int(input_txt[i][1][0]) - 1
        position_2 = int(input_txt[i][1][1]) - 1

        crate_stacks[position_2].extend(crate_stacks[position_1][-quantity:])
        for _ in range(quantity):
            crate_stacks[position_1].pop()

    print(answer(crate_stacks))


solution_2()
