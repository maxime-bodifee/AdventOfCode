with open("input.txt") as file:
    input_txt = file.readlines()
    for i in range(len(input_txt)):
        input_txt[i] = input_txt[i].strip("\n").split(",")

        for j in range(len(input_txt[i])):
            input_txt[i][j] = input_txt[i][j].split("-")

            for k in range(len(input_txt[i][j])):
                input_txt[i][j][k] = int(input_txt[i][j][k])


def solution_1():
    count = 0

    for i in range(len(input_txt)):
        lower_bound_1 = input_txt[i][0][0]
        upper_bound_1 = input_txt[i][0][1]

        lower_bound_2 = input_txt[i][1][0]
        upper_bound_2 = input_txt[i][1][1]

        if (lower_bound_1 >= lower_bound_2 and upper_bound_1 <= upper_bound_2) or \
                (lower_bound_2 >= lower_bound_1 and upper_bound_2 <= upper_bound_1):
            count += 1

    print(count)


def solution_2():
    count = 0

    for i in range(len(input_txt)):
        lower_bound_1 = input_txt[i][0][0]
        upper_bound_1 = input_txt[i][0][1]

        lower_bound_2 = input_txt[i][1][0]
        upper_bound_2 = input_txt[i][1][1]

        if (upper_bound_2 >= lower_bound_1 >= lower_bound_2) or \
                (upper_bound_1 >= lower_bound_2 >= lower_bound_1):
            count += 1

    print(count)


solution_2()
